from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'

browser.get(url)
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))
input = browser.find_element_by_class_name('zu-top-link-logo')
print(input.text)