import re
import requests
import urllib.error


def get_html_text(url):
    try:
        headers = {'User_Agent': 'Mozilla/4.0(compatible; MSIE 6.0; Windows nt)'}
        r = requests.get(url, headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except urllib.error.URLError as e:
        print(e.reason)
        return ""

def parse_html(ilt, html):
    try:
        plt = re.findall(r'"view_price":"[\d.]*"', html)
        til = re.findall(r'"raw_title":".*?"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(til[i].split(':')[1])
            ilt.append([price, title])
    except :
        print('失败')


def print_goods_list(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


if __name__ == '__main__':
    infolist = []
    depth = 1
    goods = '书包' #input('请输入你想查询的商品：')
    start_url = "https://s.taobao.com/search?q=" + goods
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            print(url)
            html = get_html_text(url)
            parse_html(infolist, html)
            # print(len(infolist))
            # print(infolist)
        except:
            continue
    print_goods_list(infolist)
