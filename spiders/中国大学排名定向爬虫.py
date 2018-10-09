import bs4
import requests
import urllib.error
from bs4 import BeautifulSoup
import os


def get_html_text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except urllib.error.URLError as e:
        print(e.reason)
        return ""


def fill_univ_list(ulist, html):
    soup = BeautifulSoup(html, 'lxml')  # html/xml这两种格式
    # print(soup.prettify())
    # print(soup.find('tbody'))
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag):   # 过滤掉非标签类型
            tds = tr('td')
            # print(tds)
            ulist.append([tds[0].string, tds[1].string, tds[2].string])

    # all_u = soup.find("tbody").children
    # print(all_u)
    # for tr in all_u:
    #     tds = tr.find_all('td')
    #     ulist.append([tds[0], tds[1], tds[2]])


def print_univ_list(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校名称", "省市", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))

if __name__ == '__main__':
    uinfo = []
    url = "http://www.zuihaodaxue.cn/shengyuanzhiliangpaiming2018.html"
    html = get_html_text(url)
    fill_univ_list(uinfo, html)
    print_univ_list(uinfo, 20)