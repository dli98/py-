import requests
import re
from urllib import parse
from bs4 import BeautifulSoup
from save_mongo import save_to_mongo
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed

def get_html_text(url):
    headers = {'User-Agent':
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    r = requests.get(url, headers=headers)
    try:
        r.raise_for_status()
    except Exception as e:
        print(e)
        return None
    return r.text


def municipality_directly_info(soup):
    """
    直辖市信息
    :return: 无返回值，直接出入mongoDB
    """
    print('正在解析直辖市信息')
    dds = soup.find('div', class_='hot-list clearfix').find('dd').find_all('a')  # 直辖市
    provice_info = {}
    info = []
    for a in dds:
        citys = {}
        citys['city_id'] = re.search(r'/(\d.*).html', a.attrs['href']).group(1)  # 得到这个省的编码
        citys['city_name'] = a.text
        info.append(citys)
    provice_info['citys'] = info
    provice_info['priovice_name'] = '直辖市'
    provice_info['provice_id'] = '0'
    save_to_mongo('mafengwo', provice_info)


def find_province_url(url):
    html = get_html_text(url)
    soup = BeautifulSoup(html, 'lxml')
    municipality_directly_info(soup)  # 处理直辖市信息
    dts = soup.find('div', class_='hot-list clearfix').find_all('dt')
    name = []
    provice_id = []
    urls = []
    print('正在处理非直辖市信息')
    for dt in dts:
        all_a = dt.find_all('a')
        for a in all_a:
            name.append(a.text)
            link = a.attrs['href']
            provice_id.append(re.search(r'/(\d.*).html', link).group(1))  # 得到这个省的编码
            # 得到这个省的热门城市链接
            data_cy_p = link.replace('travel-scenic-spot/mafengwo', 'mdd/citylist')
            urls.append(parse.urljoin(url, data_cy_p))
    return name, provice_id, urls


def parse_city_info(response):
    text = response.json()['list']
    soup = BeautifulSoup(text, 'lxml')
    items = soup.find_all('li', class_="item")
    info = []
    nums = 0
    for item in items:
        city = {}
        city['city_id'] = item.find('a').attrs['data-id']
        city['city_name'] = item.find('div', class_='title').text.split()[0]
        city['nums'] = int(item.find('b').text)
        nums += city['nums']
        info.append(city)
    return info, nums


def func(page, provice_id):
    print(f'解析{page}页信息')
    data = {'mddid': provice_id, 'page': page}
    response = requests.post('http://www.mafengwo.cn/mdd/base/list/pagedata_citylist', data=data)
    info, nums = parse_city_info(response)  # 得到每个景点城市的具体名字, 链接, 多人少去过
    return (info, nums)


def parse_city_url(html, provice_id):
    provice_info = {}
    soup = BeautifulSoup(html, 'lxml')
    pages = int(soup.find(class_="pg-last _j_pageitem").attrs['data-page'])  # 这个省总共有多少页热门城市
    city_info = []
    sum_nums = 0  # 用来记录这个省的总流量
    tpool = ThreadPoolExecutor(20)
    obj = []
    for page in range(1, pages + 1):  # 解析页面发现是个post请求
        t = tpool.submit(func, page, provice_id)
        obj.append(t)
    for t in as_completed(obj):
        info, nums = i.result()
        sum_nums += nums
        city_info.extend(info)
    provice_info['sum_num'] = sum_nums
    provice_info['citys'] = city_info
    return provice_info


def get_city_process(url, name, provice_id):
    print(f'正在解析{url}')
    html = get_html_text(url)
    provice_info = parse_city_url(html, provice_id)
    provice_info['provice_id'] = provice_id
    provice_info['provice_name'] = name
    print(f'存储{name}省的信息')
    save_to_mongo('mafengwo', provice_info)

def get_city_id():
    url = 'http://www.mafengwo.cn/mdd/'
    name, provice_id, urls = find_province_url(url)
    Ppool = ProcessPoolExecutor(5)
    for url, name, provice_id in zip(urls, name, provice_id):
        Ppool.submit(get_city_process, url, name, provice_id)
    Ppool.shutdown()



if __name__ == '__main__':
    get_city_id()
