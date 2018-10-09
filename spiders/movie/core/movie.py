from multiprocessing.pool import Pool
from multiprocessing import Queue
import requests
import json
from urllib.parse import urlencode
from requests.exceptions import ConnectionError
import pymongo

client = pymongo.MongoClient('localhost')
db = client['douban']


def get_html_text(offset):
    data = {
        'sort': 'T',
        'range': '0,10',
        'tags': '',
        'start': offset
    }
    url = 'https://movie.douban.com/j/new_search_subjects?' + urlencode(data)
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
        return None
    except ConnectionError:
        print('抓取失败')
        return None


def parse_html_info(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield {
                'directors': item.get('directors'),
                'rate': item.get('rate'),
                'cover_x': item.get('cover_x'),
                'star': item.get('star'),
                'title': item.get('title'),
                'url': item.get('url'),
                'casts': item.get('casts'),
                'cover': item.get('cover'),
                'id': item.get('id'),
                'cover_y': item.get('cover_y')
            }


def save_to_mongo(result):
    if db['movie_info'].update({'id': result['id']}, {'$set': result}, True):
        print('存入MONGODB成功')
        return True
    return False


def hot_movie(offset):
    html = get_html_text(offset)
    for result in parse_html_info(html):
        save_to_mongo(result)

