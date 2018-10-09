from multiprocessing.managers import BaseManager
from Html_Downloader import Html_Downloader
from Html_Parser import Html_Parser


class SpiderWork(object):
    def __init__(self):
        # 初始化分布式进程工作节点的连接作业
        # 实现第一步：使用BaseManager注册用于获取Queue的方法名称
        BaseManager.register('get_task_queue')
        BaseManager.register('get_result_queue')
        # 实现第二步，连接到服务器
        server_addr = '192.168.43.149'
        print(f'connect to server {server_addr}...')
        self.m = BaseManager(address=(server_addr, 8001), authkey=b'baike')
        # 从网络连接
        self.m.connect()
        # 实现第三步：获取Queue的对象
        self.task = self.m.get_task_queue()
        self.result = self.m.get_result_queue()
        # 初始化网页下载器和解析器
        self.downloader = Html_Downloader()
        self.parser = Html_Parser()
        print('init finish')

    def crawl(self):
        while 1:
            try:
                if not self.task.empty():
                    url = self.task.get()
                    if url == 'end':
                        print('控制节点通知爬虫节点停止工作...')
                        # 接的通知其他节点停止工作
                        self.result.put({'new_urls': 'end', 'data': 'end'})
                        return
                    print('爬虫节点正在解析%s' % url.encode('utf-8'))
                    content = self.downloader.download(url)
                    new_urls, data = self.parser.parser(url, content)
                    # print(new_urls)
                    self.result.put({'new_urls': new_urls, 'data': data})
            except EOFError as e:
                print(e, '连接工作节点失败')
            except Exception as e:
                print(e)
                print('Crawl fail')

if __name__ == '__main__':
    spider = SpiderWork()
    spider.crawl()