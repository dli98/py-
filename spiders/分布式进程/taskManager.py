import queue
import socket
from socket import SOL_SOCKET, SO_REUSEADDR
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
# 任务个数
task_number = 10
# 定义收发队列
task_queue = queue.Queue(task_number)
result_queue = queue.Queue(task_number)


def get_task():
    return task_queue


def get_result():
    return result_queue


# 创建类似的queueManager：
# 从BaseManager继承的
class QueueManager(BaseManager):
    pass


def win_run():
    # windows 下绑定调用接口不能使用lambda，所以只能先定义函数再绑定
    # 把两个队列注册到网络上
    sk = socket.socket()
    QueueManager.register('get_task_queue', callable=get_task)
    QueueManager.register('get_result_queue', callable=get_result)
    # 绑定端口并设置验证口令，Windows下需要填写IP地址，Linux 下不填默认本机地址
    sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    manager = QueueManager(address=('192.168.43.149', 8001), authkey=b'qiye')
    # 启动
    manager.start()
    try:
        # 通过网络获取任务队列和结果队列
        task = manager.get_task_queue()
        result = manager.get_result_queue()
        # 添加任务
        for url in ["ImageUrl_"+str(i) for i in range(10)]:
            print(f'put task {url}...')
            task.put(url)
        print('try get result...')
        for i in range(10):
            print(f'result is {result.get(timeout=100)}')
    except:
        print('Manager error')
    finally:
        # 一定要关闭，否则会报管道未关闭的错误
        manager.shutdown()


if __name__ == '__main__':
    # Windos 下多进程可能会有问题，添加这句可以缓解
    freeze_support()
    win_run()