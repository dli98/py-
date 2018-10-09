import csv
import re
import requests
from lxml import etree
# 第三方库User-Agent模块，它提供了最新、最全的浏览器的标识
# 支持谷歌、火狐、IE、Opera
# 使用命令pip3 install fake-useragent安装
from fake_useragent import UserAgent


class DBMovie(object):
    def __init__(self):
        self.base_url = 'https://movie.douban.com/top250'
        # self.ua = UserAgent()
        self.html_obj = None

    def open_file(self):
        csv_file = open('movie.csv', 'w', encoding='utf-8', newline='')
        self.writer = csv.DictWriter(
            csv_file,
            fieldnames=[
                'movie_rank', 'movie_name', 'movie_member', 'movie_star', 'movie_comment', 'movie_quote'
            ]
        )
        self.writer.writeheader()

    def get_next_page_url(self):
        a = self.html_obj.xpath('//span[@class="next"]/a')
        if len(a) == 0:
            print('已经是最后一页')
            return
        next_page = a[0].xpath('@href')[0]
        # next_page：?start=50&filter=
        self.get_page_code(next_page)

    def write_movie_info(self, movie_list):
        for index, moive in enumerate(movie_list):
            self.writer.writerow(moive)
            print('第{}页写入完成'.format(index))
        self.get_next_page_url()

    def get_content_by_xpath(self, html_obj):
        movie_list = []
        item_div = html_obj.xpath('//div[@class="item"]')
        for item_tag in item_div:
            movie_dict = {}

            em = item_tag.xpath('.//em/text()')[0]
            print(em)
            hd = item_tag.xpath('.//div[@class="hd"]/a/span/text()')
            # 将hd中的3个信息拼接在一起
            info = ''
            for info_text in hd:
                content = info_text.strip('\n').strip()
                info += content
            # 演员
            member_info = item_tag.xpath('.//p[@class=""]/text()')[0].strip('\n').strip()
            # 电影评分
            star_number = item_tag.xpath('.//span[@class="rating_num"]/text()')[0]
            # 电影评论
            comment_number = item_tag.xpath('.//div[@class="star"]/span[last()]/text()')[0]
            comment_number = re.search(re.compile('(\d+)'), comment_number).group(1)
            # 电影点评
            quote = item_tag.xpath('.//span[@class="inq"]')
            if len(quote) != 0:
                quote = quote[0].xpath('text()')[0]
            else:
                quote = '影评不存在'

            # 将以上数据添加到movie_dict里
            movie_dict['movie_rank'] = em
            movie_dict['movie_name'] = info
            movie_dict['movie_member'] = member_info
            movie_dict['movie_star'] = star_number
            movie_dict['movie_comment'] = comment_number
            movie_dict['movie_quote'] = quote

            movie_list.append(movie_dict)

        self.write_movie_info(movie_list)

    def get_page_code(self, url=""):
        # abs_url：请求的绝对路径
        # 第2页 url = ?start=25&filter=
        # 第2次请求abs_url = https://www.douban.com/top250 + ?start=50&filter=
        abs_url = self.base_url + url
        content = requests.get(abs_url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
        }).content.decode()
        print(content)

        # 把网页源代码解析成文档树对象
        self.html_obj = etree.HTML(content, parser=etree.HTMLParser(encoding='utf-8'))

        # 调用get_content_by_xpath()
        self.get_content_by_xpath(self.html_obj)


if __name__ == "__main__":
    movie_obj = DBMovie()
    movie_obj.open_file()
    movie_obj.get_page_code()
