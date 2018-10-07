import requests
from bs4 import BeautifulSoup

html = requests.get("http://www.pythonscraping.com/pages/page3.html")

soup = BeautifulSoup(html.text, "html.parser")


prince_list = soup.findAll(lambda tag: len(tag.attrs) == 2)
for i in prince_list:
    print(i)

print(len(prince_list))
