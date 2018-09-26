# 容器序列
    # list，tuple，collection.deque
    # 存放的是他们所包含的任意对象的引用
# 扁平序列
    # str，bytes，bytearray，memoryview和array.array
    # 存放的是值，扁平序列其实是一段连续的内存空间

# 可变序列
    # list，
# 不可变序列
    # tuple，str和bytes

text = [i for i in range(10)]  # 列表推导式，如果超过二行，考虑for循环
print(text)                    # 列表推导的作用只用一个：生成列表


text = (i for i in range(10))  # 生成表达式，只不过把方括号换成圆括号而已
print(text)


text = tuple(i for i in range(10))  # 生成表达式是一个函数调用过程中的唯一参数时，那么不需要
print(text)                         # 用额外的括号把它围起来


# 用*处理剩下的元素    在平行赋值中，*前缀只能出现在一个变量前面
# 1 函数
    # def main(*args, **kwargs):
    # 在python中，函数用*args来获取不确定数量的位置参数，**kwargs获取不确定数量的关键字传参

# 2 元组
a, b , *rest = range(5)
print(a, b, rest)


# 列表或元祖的方法和属性
#                          列表          元组
# s.__add__(s2)             *             *       s+s2 拼接 ————创建一个新对象
# s.__iadd__(s2)            *                     s += s2，就地拼接————元祖不可变
# s.append(e)               *
# s.clear()                 *                     删除所有元素
# s.__contain(e)            *             *       s是否包含e————一般使用in
# s.count(e)                *             *       e在s中出现的次数
# s.extend(it)              *                     把可迭代对象it追加给s
# s.index(e)                *             *       在s中找到元素e第一次出现的位置
# s.insert(p, e)            *                     在位置p之前插入元素e
# s.pop([p])                *                     删除最后或位于p位置的元素，并返回他的值
# s.remove(e)               *                     删除s中第一次出现的e
# s.reverse()               *                     就地把s的元素倒序排列
# s.sort([key], [reverse])  *                     就地对s的元素进行排序
# sorted内置函数，可接受任何可迭代对象，最后返回一个列表。




# 当数组不是首选时
    # 存放大量float，数组array效率更高
    # 频繁的对序列做先进先出的操作，deque(双端队列)的速度会更快
    # 如果查找操作很频繁，用set会更合适
