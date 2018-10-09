import requests
from bs4 import BeautifulSoup
from visual import read_mongo
from save_mongo import db, MONGO_DB, city_info_to_mongo
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process


class city_detail_deal:
    def __init__(self):
        df = read_mongo(db, MONGO_DB, {'_id': 0, 'citys': 1})
        self.id = df['city_id']
        self.name = df['city_name']

    @staticmethod
    def get_html_soup(self, url):
        headers = {'User-Agent':
                       'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        r = requests.get(url, headers=headers)
        try:
            r.raise_for_status()
        except Exception as e:
            print(e)
            return None
        soup = BeautifulSoup(r.text, 'lxml')
        return soup

    def get_city_food(self, id_):
        url = 'http://www.mafengwo.cn/cy/' + id_ + '/gonglve.html'
        print(f'正在解析{url}')
        soup = self.get_html_soup(url)
        list_rank = soup.find('ol', class_='list-rank')
        food = [k.text for k in list_rank.find_all('h3')]
        food_count = [int(k.text) for k in list_rank.find_all('span', class_='trend')]
        food_info = []
        for i, j in zip(food, food_count):
            fd = {}
            fd['food_name'] = i
            fd['food_count'] = j
            food_info.append(fd)
        return food_info

    def get_city_jd(self, id_):
        """
        :param id_:城市编码id
        :return: 景点名称和评论数量
        """
        url = 'http://www.mafengwo.cn/jd/' + id_ + '/gonglve.html'
        print(f'正在解析{url}')
        soup = self.get_html_soup(url)
        jd_info = []
        try:
            all_h3 = soup.find('div', class_='row-top5').find_all('h3')
        except:
            print('没有景点')
            jd = {}
            jd['jd_name'] = ''
            jd['jd_count'] = 0
            jd_info.append(jd)
            return jd_info
        for h3 in all_h3:
            jd = {}
            jd['jd_name'] = h3.find('a')['title']
            try:
                jd['jd_count'] = int(h3.find('em').text)
            except:
                print('没有评论')
                jd['jd_count'] = 0
            jd_info.append(jd)
        return jd_info

    def func(self, id_, name):
        try:
            food_info = self.get_city_food(id_)
        except Exception as e:
            print(e, '没有特色食物')
        jd_info = self.get_city_jd(id_)
        city_info_to_mongo('city_detail', {'city_name': name,
                                           'food': food_info,
                                           'jd': jd_info
                                           })

    def get_detail_info(self):
        tpool = ThreadPoolExecutor(max_workers=20)
        for id_, name in zip(self.id, self.name):
            tpool.submit(self.func, id_, name)
        tpool.shutdown()




class Schedule(object):
    c = city_detail_deal()



if __name__ == '__main__':
    c = city_detail_deal()
    c.get_detail_info()
