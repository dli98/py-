import bs4
import requests
import urllib.error
from bs4 import BeautifulSoup
import os
import random
import re

user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
    "Mozilla/5.0 (Windows NT 10.0; WOW64)",
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/51.0.2704.63 Safari/537.36'
    ]


def get_html_text(url, page):
    try:
        headers = {'User-Agent': user_agents[-1],
                   'Host': '400.haodf.com'
                   }
        kv = {'nowpage': page}
        r = requests.get(url, headers=headers, params=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print(e)
        return ""


def parse_doc_info(ulis, html):
    soup = BeautifulSoup(html, 'lxml')
    all_info = soup.find_all(class_='clearfix showResult-cell bb pb10 mt15')
    for p in all_info:
        try:
            tc_p = p.find('p', class_='tc mt5')
            name = tc_p.find('a').text
            grade = re.findall(r'</a>.*<!', str(tc_p))[0][4:-2]
            fb_p = p.find('p', class_='fb').text.split()
            print(fb_p[0], grade)
            ulis.append([name, grade, fb_p[0], fb_p[1]])
            # print(fb_p[0], fb_p[1])
        except:
            continue


def print_doc_list(ulist):
    tplt = "{0:{4}^10}\t{1:{4}^20}\t{2:{4}^20}\t{3:{4}^10}"
    print(tplt.format("医生姓名", "医生等级", "医院", "科室", chr(12288)))
    for i in range(len(ulist)):
        u = ulist[i]
        # print(tplt.format(u[0], u[0], u[0], chr(12288)))
        print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))

if __name__ == '__main__':
    info = []
    url = "https://400.haodf.com/index/search"
    for i in range(1, 3):
        html = get_html_text(url, i)
        parse_doc_info(info, html)
    print_doc_list(info)


