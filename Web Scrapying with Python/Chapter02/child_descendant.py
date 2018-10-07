# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
#
# data = BeautifulSoup(html, "html.parser")
#
# for child in data.find("table", {"id": "giftList"}).children:
#     print(child)

import requests
from bs4 import BeautifulSoup

html = requests.get("http://www.pythonscraping.com/pages/page3.html")

soup = BeautifulSoup(html.text, "html.parser")

# children     list_iterator
print(type(soup.find("table", {"id": "giftList"}).children))
# include '\n'
print(len(list(soup.find("table", {"id": "giftList"}).children)))
print(len(list(soup.find("table", {"id": "giftList"}).descendants)))
for child in soup.find("table", {"id": "giftList"}).children:
    print(repr(child))
    print('*************')
