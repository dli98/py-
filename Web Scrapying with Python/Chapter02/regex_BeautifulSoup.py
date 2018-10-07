import requests

from bs4 import BeautifulSoup

import re

html = requests.get("http://www.pythonscraping.com/pages/page3.html")

soup = BeautifulSoup(html.text, "html.parser")

images = soup.findAll("img", {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")})

for i in images:
    print(i["src"])
