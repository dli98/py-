from selenium import webdriver
import re
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *
import pymongo
# from selenium.webdriver.chrome.options import Options

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome(chrome_options=chrome_options)
# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
wait = WebDriverWait(browser, 10)

# browser.set_window_size(1400, 900)


def search():
    try:
        browser.get('https://www.taobao.com')
        input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        input.send_keys('美食')
        submit.click()
        total = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'total')))
        get_products()
        return total.text
    except TimeoutException:
        return search()


def next_page(page_number):
    try:
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.next > a > span:nth-child(1)')))
        submit.click()
        num = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page_number)))
        print(f'正在解析第{page_number}页')
        get_products()
    except TimeoutException:
        next_page(page_number)


def get_products():
    product = {}
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    items = soup.select('#mainsrp-itemlist .items .item')
    # item = soup.find_all(class_='item')
    for item in items:
        product = {
            'image': item.select('.pic .img')[0]['data-src'],
            'price': item.find(class_='price').text.strip(),
            'deal': item.find(class_='deal-cnt').text[: -3],
            'title': item.find(class_='title').text.strip(),
            'shop': item.find(class_='shop').text.strip(),
            'location': item.find(class_='location').text
        }
        save_to_mongo(product)


def save_to_mongo(result):
    try:
        if db[MONGO_DB].insert(result):
            print('存储到MONGODB成功')
    except Exception:
        print('存储失败')


def main():
    total = search()
    total = int(re.search('(\d+)', total).group(1))
    for i in range(2, total+1):
        next_page(i)


if __name__ == '__main__':
    main()