from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)


def search():
    browser.get('https://www.baidu.com/')
    input = wait.until(EC.presence_of_element_located((By.ID, 'kw')))
    submit = wait.until(EC.element_to_be_clickable((By.ID, 'su')))
    input.send_keys('qq邮箱')
    submit.click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="1"]/h3/a[1]'))).click()
    browser.implicitly_wait(10)
    browser.switch_to_window(browser.window_handles[1])
    browser.switch_to_frame('login_frame')
    wait.until(EC.presence_of_element_located((By.ID, 'switcher_plogin'))).click()
    u = wait.until(EC.presence_of_element_located((By.ID, 'u')))
    p = wait.until(EC.presence_of_element_located((By.ID, 'p')))
    u.send_keys('942203701')
    p.send_keys('xingfu1314...')
    wait.until(EC.element_to_be_clickable((By.ID, 'login_button'))).click()


def main():
    search()


if __name__ == '__main__':
    main()