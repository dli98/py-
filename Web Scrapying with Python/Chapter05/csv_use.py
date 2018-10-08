import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
soup = BeautifulSoup(html, 'lxml')
table = soup.find('table', {'class': 'wikitable'})
print(type(table))
rows = table.findAll('tr')

csvFile = open("editors.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.text)
        writer.writerow(csvRow)
finally:
    csvFile.close()