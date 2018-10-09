import re
import requests
import traceback
import os
from bs4 import BeautifulSoup


def get_html_text(url, code='utf-8'):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        print('失败')
        return ""


def get_stock_list(lst, stockurl):
    """
     从东方财富网获取股票列表
    :param lst:
    :param stockurl:
    """
    html = get_html_text(stockurl, 'GB2312')
    soup = BeautifulSoup(html, 'lxml')
    all_a = soup.find_all('a')
    for i in all_a:
        try:
            print(type(i))
            href = i.attrs['href']
            # print(type(href))
            lst.append(re.findall(r'[s][hz]\d{6}', href)[0])
            # print(type(re.findall(r'[s][hz]\d{6}', href)[0]))
        except:
            continue


def get_stock_info(lst, stockurl, fpath):
    count = 0
    for stock in lst:
        url = stockurl + stock + ".html"
        html =get_html_text(url)
        try:
            if html =='':
                continue
            info_dict = {}
            soup = BeautifulSoup(html, 'lxml')
            stock_info = soup.find('div', class_='stock-bets')
            # print(type(stock_info))   find()返回的是个标签
            name = stock_info.find(class_='bets-name')
            # print(name.text)
            info_dict.update({'股票名称': name.text.split()[0]})

            keylist = stock_info.find_all('dt')
            # print(type(keylist))   find_all返回的是结果集
            valuelist = stock_info.find_all('dd')
            for i in range(len(keylist)):
                key = keylist[i].text
                val = valuelist[i].text
                info_dict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(info_dict) + '\n')
                count = count + 1
                print('当前速度:{:.2%}'.format(count/len(lst)), end='\r')

        except:
            count = count + 1
            print('当前速度:{:.2%}'.format(count/len(lst)), end='\r')
            traceback.print_exc()
            continue


if __name__ == '__main__':
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'D://BaidustockInfo.txt'
    if os.path.exists(output_file):
        os.remove(output_file)
        print('删除同名文件')
    slist = []
    get_stock_list(slist, stock_list_url)
    get_stock_info(slist, stock_info_url, output_file)