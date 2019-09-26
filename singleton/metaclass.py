class SingletonType(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__call__(*args, **kwargs)  # 创建一个类对象
        return cls._instance


class Foo(metaclass=SingletonType):
    def __init__(self, name):
        self.name = name

obj1 = Foo('name1')
obj2 = Foo('name2')
obj3 = Foo('name3')
print(obj1, obj2, obj3)
print(obj1.name, obj2.name, obj3.name)

