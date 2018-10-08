from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def ngrams(indata, n):
    # indata = re.split(r' |,|;|\n|', indata)
    indata = indata.split()
    print(indata)
    outodata = []

    for i in range(len(indata) - n + 1):
        outodata.append(indata[i:i + n])
        print(outodata)
        break

    return outodata


html = urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
soup = BeautifulSoup(html, "html.parser")

content = soup.find("div", {"id": "mw-content-text"}).get_text()
# content = soup.find("div", id_="mw-content-text").get_text()

ngram = ngrams(content, 2)

print(ngram)
print("2-ngrams count is:" + str(len(ngram)))
