import requests
from bs4 import BeautifulSoup
import re

html = requests.get("https://en.wikipedia.org/wiki/Kevin_Bacon")

soup = BeautifulSoup(html.text, "html.parser")

'''
for link in data.findAll("a"):
    if 'href'  in link.attrs:
        print(link.attrs['href'])
'''

for link in soup.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
