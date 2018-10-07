import requsets
from bs4 import  BeautifulSoup


html = requsets.get("http://www.pythonscraping.com/pages/page1.html")

'''
To get rid of this warning, change this:
 BeautifulSoup([your markup])
to this:
 BeautifulSoup([your markup], "html.parser")
  markup_type=markup_type))
'''
#data = BeautifulSoup(html.read())

soup = BeautifulSoup(html.text, "html.parser")


print(soup.title)
