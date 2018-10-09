from Data_Output import Data_Output
from Html_Downloader import Html_Downloader
from Html_Parser import Html_Parser
from URL_Manager import URL_Manager


class SpiderMan(object):
    def __init__(self):
        self.mamager = URL_Manager()
        self.downloader = Html_Downloader()
        self.parser = Html_Parser()
        self.output = Data_Output()

    def crawl(self, root_url):
        # 添加入口URL
        self.mamager.add_new_url(root_url)
        # 判断url管理器中是否有新的url, 同时判断抓取了多少个url
        while (self.mamager.has_new_url() and self.mamager.old_url_size()<100):
            try:
                # 从URL管理器获取新的url
                new_url = self.mamager.get_new_url()
                html = self.downloader.download(new_url)
                # 从html解析器抽取网页数据
                new_url, data = self.parser.parser(new_url, html)
                # 将抽取的url 添加到URL管理器中
                # print(new_url, data)
                self.mamager.add_new_urls(new_url)
                # 数据存储器存储文件
                # print('***************8')
                self.output.store_data(data)

                print(f"已经抓取{self.mamager.old_url_size()}个链接")
            except Exception as e:
                print(e)
        self.output.output_html()

if __name__ == '__main__':
    spider_man = SpiderMan()
    spider_man.crawl("http://baike.baidu.com/view/284853.htm")
