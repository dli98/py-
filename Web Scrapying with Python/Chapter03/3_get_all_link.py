from bs4 import BeautifulSoup
import requests
import re

pages = set()


def getLinks(articeUrl):
    global pages

    html = requests.get("https://en.wikipedia.org" + articeUrl)
    data = BeautifulSoup(html.text, "html.parser")

    try:
        print(data.h1.text)
        print(data.find(id="mw-content-text").findAll("p")[0])
        print(data.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("Missing some attributes")

    for link in data.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print("new Page:")
                print(newPage)

                pages.add(newPage)

                getLinks(newPage)


getLinks("")
