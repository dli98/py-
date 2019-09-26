import threading
import time


class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = super(Singleton, cls).__new__(cls)
        return Singleton._instance


def task(arg):
    obj = Singleton(arg)
    print(obj)


for i in range(20):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
