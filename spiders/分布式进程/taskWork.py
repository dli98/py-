import time
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass
# 第一步，使用QueueManager 注册用于获取Queen的方法名称
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
# 第二步，链接服务器
server_addr = '192.168.43.149'
print(f'Connect to server {server_addr}')
# 端口和验证口令注意保持与服务进程完全一致：
m = QueueManager(address=(server_addr, 8001), authkey=b'qiye')
# 从网络链接：
m.connect()
# 第三步：获取queue的对象
task = m.get_task_queue()
result = m.get_result_queue()
# 第四步，从task队列中获取任务，并把结果写入result队列：
while (not task.empty()):
    immage_url = task.get(True, timeout=20)
    print(f'run task download {immage_url}...')
    time.sleep(1)
    result.put(f'{immage_url}--->success')

# 处理结束：
print('worker exit.')

