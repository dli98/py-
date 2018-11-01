import re
import requests
from bs4 import BeautifulSoup
import time


def get_frist(page, s):
    params = {
        'keyword': '小米手机',
        'enc': 'utf-8',
        'qrst': '1',
        'rt': '1',
        'stop': '1',
        'vt': '2',
        'bs': '1',
        'psort':'3',
        'ev': 'exbrand_小米（MI）^',
        'page': str(page),
        's': s,
        'click': '0',
    }
    url = 'https://search.jd.com/Search?'
    try:
        r = requests.get(url, params=params)
        r.raise_for_status()
        r.encoding = 'utf-8'
        print(r.url)
        return r.text
    except Exception as e:
        print(r.status_code)


def get_last(page, s):
    log_id = time.time()
    log_id = '%.5f' % log_id
    params = {
        'keyword': '小米手机',
        'enc': 'utf-8',
        'qrst': '1',
        'rt': '1',
        'stop': '1',
        'vt': '2',
        'bs': '1',
        'psort': '3',
        'ev': 'exbrand_小米（MI）^',
        'page': str(page),
        's': s,
        'scrolling': 'y',
        'log_id': log_id,
        'tpl': '3_M',
    }
    url = 'https://search.jd.com/Search?'
    try:
        r = requests.get(url, params=params)
        r.raise_for_status()
        r.encoding = 'utf-8'
        print(r.url)
        return r.text
    except Exception as e:
        print(r.status_code)


def get_info(text, count):
    soup = BeautifulSoup(text, 'html.parser')
    for child in soup.find_all(class_='gl-item'):
        data = {}
        try:
            data['price'] = child.find('strong').attrs['data-price']
        except:
            data['price'] = child.find('strong').find('i').text

        try:
            data['shop'] = child.find(class_='p-shop').find('a').text.strip()
        except:
            print('这是一个广告')
            continue

        try:
            data['name'] = child.find(class_='p-name').find('em').text
            data['commit'] = child.find(class_='p-commit').find('strong').find('a').text
        except:
            continue
        print(data)
        save_to_file(data)
        count += 1
        if count == 200:
            break
    return count


def save_to_file(data):
    file = 'goods.txt'
    with open(file, 'a', encoding='utf-8') as f:
        f.write(str(data))
        f.write('\n')


if __name__ == '__main__':
    # text = get_frist()
    s = 1
    count = 0
    for i in range(0, 10, 2):
        text = get_frist(i, s)
        s = s + 30
        count = get_info(text, count)
        if count == 200:
            print('200个信息爬取完毕')
            break

        text = get_last(i+1, s)
        s = s + 30
        count = get_info(text, count)
        if count == 200:
            print('200个信息爬取完毕')
            break
