import queue   # queue.Queue  进程内部通信
from multiprocessing import Queue  # 跨进程通信队列
from multiprocessing import Process
# from multiprocessing import Manager
from multiprocessing.managers import BaseManager
# from multiprocessing import freeze_support
from URL_Manager import URL_Manager
from Data_Output import Data_Output
import time
# # 任务个数
# task_number = 10


def get_task():
    return url_q


def get_result():
    return result_q


# 创建类似的queueManager：
# 从BaseManager继承的
class QueueManager(BaseManager):
    pass


class NodeManager:
    def start_Manager(self, url_q, result_q):
        # windows 下绑定调用接口不能使用lambda，所以只能先定义函数再绑定
        # 把两个队列注册到网络上
        QueueManager.register('get_task_queue', callable=get_task)
        QueueManager.register('get_result_queue', callable=get_result)
        # 绑定端口并设置验证口令，Windows下需要填写IP地址，Linux 下不填默认本机地址
        manager = QueueManager(address=('192.168.43.149', 8001), authkey=b'baike')
        # 启动
        return manager

    def url_manager_pro(self, url_q, conn_q, root_url):
        url_manager = URL_Manager()
        url_manager.add_new_url(root_url)
        while True:
            while (url_manager.has_new_url()):
                # 从URL管理器获取新的URL
                new_url = url_manager.get_new_url()
                # 将新的URL 发给工作结点
                url_q.put(new_url)
                print(f'old_url = {url_manager.old_url_size()}')
                # 加一个判断条件，当爬取2000个链接后就关闭，并保存进度
                if(url_manager.old_url_size()>10):
                    # 通知爬虫节点工作结束
                    url_q.put('end')
                    print('控制节点发起结束通知')
                    # 关闭管理结点，同时存储set状态
                    url_manager.save_process('new_urls.txt', url_manager.new_urls)
                    url_manager.save_process('old_urls.txt', url_manager.old_urls)
                    return
                # 将从result_solve_proc 获取到的URl添加到URL管理器
            try:
                if not conn_q.empty():
                    urls = conn_q.get()
                    # print(urls)
                    url_manager.add_new_urls(urls)
                    if url_manager.has_new_url() == 0:
                        url_q.put('end')
                        print('控制节点发起结束通知')
                        # 关闭管理结点，同时存储set状态
                        url_manager.save_process('new_urls.txt', url_manager.new_urls)
                        url_manager.save_process('old_urls.txt', url_manager.old_urls)
                        return

            except BaseException as e:
                print(e)
                print('****************')
                time.sleep(0.1)

    def result_solve_proc(self, result_q, conn_q, store_q):
        while True:
            try:
                if not result_q.empty():
                    content = result_q.get(True)
                    if content['new_urls'] == 'end':
                        # 结果分析进程接受通知然后结束
                        print('结果分析进程接受通知然后结束：')
                        store_q.put('end')
                        return
                    conn_q.put(content['new_urls'])  # url 为set 类型
                    # print(content['new_urls'])
                    store_q.put(content['data'])  # 解析出来的数据为dict类型
                else:
                    time.sleep(0.1)    # 延时休息
            except BaseException as e:
                print(e)
                time.sleep(0.1)

    def store_pro(self, store_q):
        output = Data_Output()
        while True:
            if not store_q.empty():
                data = store_q.get()
                # print(data)
                if data == 'end':
                    print('存储进程接受通知然后结束！')
                    output.ouput_end(output.filepath)
                    return
                output.store_data(data)
            else:
                time.sleep(0.1)


if __name__ == '__main__':
    # 定义收发队列
    url_q = Queue()
    # 接受结果的队列
    result_q = Queue()
    store_q = Queue()
    conn_q = Queue()
    # 创建分布式管理器
    node = NodeManager()
    manager = node.start_Manager(url_q, result_q)
    # 创建URL管理器进程，数据提取进程和数据存储进程
    url_manager_proc = Process(target=node.url_manager_pro,
                               args=(url_q, conn_q, 'http://baike.baidu.com/view/284853.htm',))
    result_solve_proc = Process(target=node.result_solve_proc,
                                args=(result_q, conn_q, store_q,))
    store_proc = Process(target=node.store_pro,
                         args=(store_q,))

    # 启动3个进程和分布式管理器
    url_manager_proc.start()
    result_solve_proc.start()
    store_proc.start()
    # serve_forever()  服务器一直运行
    manager.get_server().serve_forever()

