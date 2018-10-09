import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import pymongo
client = pymongo.MongoClient('localhost')
db = client['jianshu']
data = []


def get_first_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    try:
        r = requests.get(url, headers=headers)

        if r.status_code == 200:
            return r.text
        return None
    except ConnectionError:
        print('抓取失败', url)
        return None


def get_page(url):
    headers = {
        'X-CSRF-Token': '6vJnbFxpgkYWu28t+TQd77DYYeG/HuELzV4vKveTleCyCWtAFd408Un7Z5cwn3b1hzZB3uGqzUQprnJKOL3lgw==',
        'X-PJAX': 'true',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return r.text
        return None
    except ConnectionError:
        print('抓取失败', url)
        return None


def save_to_mongo(result):
    db['result'].insert(result)


def parse_first_page(html):
    global data
    soup = BeautifulSoup(html, 'lxml')
    note_list = soup.find('ul', class_='note-list')
    if note_list is None:
        return None
    for li in note_list.find_all('li'):
        try:
            id = 'seen_snote_ids%5B%5D=' + li.get('data-note-id')
            data.append(id)
            yield {
                'title': li.find('div').find('a').text,
                'abstract': li.find('p').text,
                'nickname': li.find(class_='meta').find(class_='nickname').text
            }
        except:
            continue


def parse_page(html):
    global data
    soup = BeautifulSoup(html, 'lxml')
    for li in soup.find_all('li'):
        try:
            id = 'seen_snote_ids%5B%5D=' + li.get('data-note-id')
            data.append(id)
            yield {
                'title': li.find('div').find('a').text,
                'abstract': li.find('p').text,
                'nickname': li.find(class_='meta').find(class_='nickname').text
            }
        except:
            continue


def main():
    global data
    # 第一次请求
    print('正在解析第一页')
    url = 'https://www.jianshu.com/?&page=1'
    html = get_first_page(url)
    if html is None:
        return False
    for result in parse_first_page(html):
        save_to_mongo(result)
    # 弟二三请求都是get请求
    # 后面是post请求
    print('解析分页数据')
    for i in range(2, 16):
        params = '&'.join(data)
        url = 'https://www.jianshu.com/?' + params + '&page={}'.format(i)
        html = get_page(url)
        for result in parse_page(html):
            save_to_mongo(result)


if __name__ == '__main__':
    main()