import threading

import time


class Singleton(object):
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with Singleton._instance_lock:
            if not hasattr(Singleton, "_instance"):
                Singleton._instance = super(Singleton, cls).__new__(cls)
        return Singleton._instance


def task(arg):
    obj = Singleton(arg)
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
