import json
import os
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
import re
from multiprocessing import Pool
from hashlib import md5
from json.decoder import JSONDecodeError


def get_page_index(offset, keyword):
    data = {
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'format': 'json',
        'keyword': keyword,
        'offset': offset,
    }
    params = urlencode(data)
    base = 'http://www.toutiao.com/search_content/'
    url = base + '?' + params
    print(url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print('Error occurred')
        return None


def download_image(url):
    print('Downloading', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_image(response.content)
        return None
    except ConnectionError:
        return None


def save_image(content):
    file_path = '{0}'.format(os.getcwd() + '\今日头条照片')
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    image_path = '{0}/{1}.{2}'.format(os.getcwd() + '\今日头条照片', md5(content).hexdigest(), 'jpg')
    if not os.path.exists(image_path):
        with open(image_path, 'wb') as f:
            f.write(content)
            f.close()


def parse_page_index(text):
    try:
        data = json.loads(text)
        if data and 'data' in data.keys():
            for item in data.get('data'):
                yield item.get('article_url')
    except JSONDecodeError:
        pass


def get_page_detail(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print('Error occurred')
        return None


def parse_page_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    result = soup.select('title')
    title = result[0].get_text() if result else ''
    images_pattern = re.compile('gallery: JSON.parse\("(.*)"\)', re.S)
    result = re.search(images_pattern, html)
    if result:
        data = json.loads(result.group(1).replace('\\', ''))
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            for image in images:
                download_image(image)
            return {
                'title': title,
                'url': url,
                'images': images
            }


# def save_to_mongo(result):
#     if db[MONGO_TABLE].insert(result):
#         print('Successfully Saved to Mongo', result)
#         return True
#     return False


def main(offset):
    KEYWORD = '街拍'
    text = get_page_index(offset, KEYWORD)
    urls = parse_page_index(text)
    for url in urls:
        if url != None:
            html = get_page_detail(url)
            result = parse_page_detail(html, url)
        # if result : save_to_mongo(result)


if __name__ == '__main__':
    # GROUP_START = 1
    # GROUP_END = 3
    main(0)
    # pool = Pool()
    # groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    # pool.map(main, groups)
    # pool.close()
    # pool.join()