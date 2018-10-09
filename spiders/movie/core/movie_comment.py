import requests
from urllib.parse import urlencode
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient('localhost')
db = client['douban']


def comment_to_mongo(collect_name, result):
    db[collect_name].insert(result)
    # print(f'{collect_name}的评论成功存入MONGODB')
    return True


async def get_html_text(offset, id_):
    data = {
        'start': offset,
        'limit': '20',
        'sort': 'new_score',
        'status': 'P',
        'comments_only': '1'
    }
    headers = {
        'Host': 'movie.douban.com',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    url = 'https://movie.douban.com/subject/' + str(id_) + '/comments?' + urlencode(data)
    print(url)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers,) as response:
                if response.status == 200:
                    t = await response.json()
                    return t
                elif response.status == 403:
                    print('重新爬取')
                    await get_html_text(offset, id_)
                else:
                    print(response.status, '爬取失败')
                    return None
    except Exception as s:
        print(s, '抓取失败')
        return None


def get_comment(name, id_, offset=0):
    loop = asyncio.get_event_loop()  # 创建一个事件环
    while True:
        tasks = [get_html_text(off * 20, id_) for off in range(offset, offset + 10)]  # 每次添加十个任务
        result, _ = loop.run_until_complete(asyncio.wait(tasks))  # 启动事件循环
        flag = 0
        for html in result:
            html = html.result()
            if html is None:
                flag = 1
                continue
            soup = BeautifulSoup(html['html'], 'lxml')
            all_comment = soup.find_all(class_='comment')
            if not all_comment:
                flag = 1
                continue
            for comment in all_comment:
                Commentator = comment.find('a', class_='').text
                votes = comment.find('span', class_='votes').text
                short = comment.find('span', class_='short').text
                comment_to_mongo(name,
                                 {
                                     '评论者': Commentator,
                                     '评论有用度': votes,
                                     '评论内容': short
                                 }
                                 )
        if flag:
            print(f'{name}的评论全部爬取完毕')
            return
        offset += 10



if __name__ == '__main__':
    get_comment('text', 27665196)
