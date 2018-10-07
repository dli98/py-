import requests
from bs4 import BeautifulSoup

html = requests.get("http://www.pythonscraping.com/pages/warandpeace.html")

soup = BeautifulSoup(html.text, "html.parser")

'''
name_list = data.findAll("span", {"class":"green"})
for name in name_list:
    print(name.get_text())
'''

prince_list = soup.findAll(text="the prince")
print(len(prince_list))
