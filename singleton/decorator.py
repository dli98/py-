def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return _singleton


@Singleton
class A(object):  # A = singleton(A)
    a = 1

    def __init__(self, x=0):
        self.x = x


obj1 = A(2)
obj2 = A(3)
print(obj1, obj2)
