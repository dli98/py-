from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://www.taobao.com')
input =browser.find_element_by_id('q')
input.send_keys('IPhone')
time.sleep(1)
input.clear()
input.send_keys('Ipad')
button = browser.find_element_by_class_name('btn-search')
button.click()