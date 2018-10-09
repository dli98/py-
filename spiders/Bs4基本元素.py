from bs4 import BeautifulSoup
import requests


url = 'http://duanziwang.com/category/%E7%BB%8F%E5%85%B8%E6%AE%B5%E5%AD%90/'
re = requests.get(url)
print(re.url)
html = re.text
soup = BeautifulSoup(html)
print(soup.attrs)
print(soup.prettify())
# print(soup.b.string)   # 标签内字符串的注释部分
# print(soup.p.string)   # 标签内非字符串
