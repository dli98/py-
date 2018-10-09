from concurrent.futures import ThreadPoolExecutor
from core.movie import hot_movie
from conf.setting import Crawl_page
from core.movie_comment import get_comment
from core.mongodb import MongoDB_Client


class Schedule:
    @staticmethod
    def get_hot_movie():
        """
        获得热门电影的id等信息
        :return:
        """
        print('正在获得热门电影')
        tpool = ThreadPoolExecutor(20)
        for x in range(Crawl_page):
            tpool.submit(hot_movie, x * 20)
        tpool.shutdown()

    @staticmethod
    def parse_comment():
        """
        获得所有评论
        :return:
        """
        print('正在获得热门电影所对应的评论')
        c = MongoDB_Client()
        infos = c.read_mongo({}, {'_id': 0, 'id': 1, 'title': 1})
        tpool = ThreadPoolExecutor(20)
        for info in infos:
            name = info.get('title')
            id_ = info.get('id')
            tpool.submit(get_comment, name, id_)
        tpool.shutdown()

    def run(self):
        print('Movie processing runing')
        movie_id_process = Schedule.get_hot_movie()
        comment_process = Schedule.parse_comment()



