from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
input = browser.find_element_by_id('kw')
input.send_keys('图片')
botton = browser.find_element_by_id('su')
botton.click()