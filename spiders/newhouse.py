import requests
from bs4 import BeautifulSoup
import time
import csv

def get_html_text(page):
    url = f'http://newhouse.nj.house365.com/house/dist-4_p-{page}/'
    print('正在解析：', url)
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.text
    except Exception as e:
        print('抓取失败', r.status_code)
        return None


def get_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    page_num = soup.find(class_='fr orderby').find('b').text
    return int(page_num)


def get_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    for mc in soup.find_all(class_='mc_list'):
        data = {}
        data['name'] = mc.find(class_='tit').find('a').text
        data['addr'] = mc.find(class_='yh_info').find_all('p')[1].text.strip().split()[0]
        data['price'] = mc.find(class_='xiang_price').text.strip().split()[0]
        try:
            data['phone'] = ''.join(mc.find(class_='pt5').find('b').text.split())
        except Exception as e:
            print('售空，没给电话号码')
            data['phone'] = 'Null'
        print(data)
        save_to_file(data)

def save_to_file(data):
    # with open('houseInfo.txt', 'a', encoding='utf-8') as f:
    #     f.write(str(data) + '\n')
    with open('houseInfo.csv', 'a', encoding='utf-8', newline ='') as f:
        writer = csv.DictWriter(f, ['name', 'phone', 'addr', 'price'])
        writer.writerow(data)


if __name__ == '__main__':
    html = get_html_text(1)
    page_num = int(get_page(html) / 15) + 2
    get_info(html)
    for i in range(2, page_num):
        html = get_html_text(str(i))
        get_info(html)
        time.sleep(3)
