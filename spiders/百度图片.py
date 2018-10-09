import requests
import os
import urllib.error
from bs4 import BeautifulSoup


class Bai_du:
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36' \
                          ' (KHTML, like Gecko)Chrome/51.0.2704.63 Safari/537.36'
        keyword = input("Input key word：")
        self.keyword = {'word': keyword}
        self.header = {'User_Agent': self.user_agent}
        self.url = "https://image.baidu.com/search/index?tn=baiduimage&" \
                   "ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0" \
                   "&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&"

    def get_html_text(self):
        try:
            r = requests.get(url=self.url, headers=self.header, params=self.keyword)
            r.raise_for_status()
            print(r.request.url)
            r.encoding = r.apparent_encoding
            self.html = r.text
        except urllib.error.URLError as e:
            print(e.reason)

    def pick_pic(self):
        print(self.html)
        soup = BeautifulSoup(self.html, 'lxml')
        img_list = soup.find('ul', class_='imglist clearfix pageNum0')
        print(img_list)
        

if __name__ == "__main__":
    spider = Bai_du()
    spider.get_html_text()
    spider.pick_pic()

# try:
#     if os.path.exists('./photo.jpg'):
#         os.remove('./photo.jpg')
#         print('删除同名文件')
#     with open('photo.jpg', 'ab+') as f:
#         f.write(r.content + b'\n')   # HTTP响应内容二进制形式
#     print("下载完成")
# except urllib.error.URLError as e:
#     print(e.reason)
#     print("爬取失败")