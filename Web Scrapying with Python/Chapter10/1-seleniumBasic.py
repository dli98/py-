from selenium import webdriver
import time

driver = webdriver.Firefox()
# driver = webdriver.PhantomJS()
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(5)
print(driver.find_element_by_id('content').text)
driver.close()