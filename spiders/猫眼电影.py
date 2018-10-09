import json
import re
from multiprocessing import Lock
from multiprocessing.pool import Pool

import requests
import os


def get_htme_text(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        # r.encoding = 'utf-8'
        return r.text
    except Exception as e:
        print(e)


def parse_html(html):
    dds = re.findall(r'<dd>.*?</dd>', html, flags=re.S)
    for dd in dds:
        try:
            title = re.findall(r'title="(.+?)"', dd)[0],
            staring = re.findall(r'star">(.*?)</p>', dd, flags=re.S)[0].split()[0],
            # print(staring)
            releasetime = re.findall(r'releasetime">(.*?)</p>', dd)[0],
            yield {
                'title': title,
                'staring': staring,
                'releasetime': releasetime
            }
        except:
            continue


def output_info(content):
    # mutex = Lock()
    # mutex.acquire()
    with open('test.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n', )
        f.close()
    # mutex.release()


def main(offset):
    info = []
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_htme_text(url)
    for item in parse_html(html):
        print(item)
        output_info(item)


if __name__ == '__main__':
    for i in range(10):
        main(i*10)
    # pool = Pool()
    # # for i in range(10):
    # #     pool.apply_async(main, args=(i*10,))
    # pool.map(main, [i * 10 for i in range(10)])
    # pool.close()
    # pool.join()




