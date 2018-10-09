import re
# group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。
# re.search(pattern= , string= , flags=0)
# 从一个字符串中搜索匹配正则表达式的第一个位置
# pattern  正则表达式的字符串或原生字符串表示
# string   待匹配字符串
# flags 正则表达式使用时的控制标记
'''
    re.I 忽略正则表达式的大小写
    re.M 给定字符串的每行当中匹配开始
    re.S 默认匹配除换行外的所以匹配
'''

# match = re.search(r'[1-9]\d{5}', 'BIT 100081 TSU 100084',)
# print(match.re)
# print(match.pos)
# print(match.endpos)
# print(match.string)
# print('xxxxxxxxx')
# print(match.group(0))
# print(match.start())
# print(match.end())
# print(match.span())
#
# print(match)
# pat = re.compile(r'')
# rst = pat.search('BIT 100081 TSU 100084')
# print(rst)
# # 函数式用法，一次性操作
# '''
# 面向对象用法：编译后的多次操作
# pat = re.compile(r'[1-9]\d{5}')  #将正则表达式的字符串形式编译成正则表达式对象
# rst = pat.search('BIT 100081')
# '''
# if match:
#     print(match.group(0))
#
# '''
# re.match(pattern, string, flags=0)
# 从一个字符串的开始位置起匹配正则表达式，返回match对象
# '''
# # match = re.match(r'[1-9]\d{5}', 'BIT 100081')
# match = re.match(r'[1-9]\d{5}', '100081 BIT')
# if match:
#     print(match.group(0))
#
#
#
# '''
# re.findall()
# 搜素字符串，以列表类型返回全部匹配的字串
# '''
#
# ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')
# ls = re.findall(r'(\+86[1][23456789]\d{9}|'
#                 r'86[1][23456789]\d{9})', '8613125134887 +8611125134887 +8613125134887')
# print(ls)
#
# '''
# re.split(pattern, string, maxsplit=0, flag=0)
# 将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
# maxsplit: 正则表达式使用时的控制标记
# '''
# ls = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084')
# print(ls)
# ls = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084', maxsplit=1)
# print(ls)
#
# '''
# re.findite()
# 搜素字符串，返回一个匹配结果的迭代类型，每个迭代元素为match对象
# '''
# for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084'):
#         print(m.group(0))
#
# '''
# re.sub(pattern, repl, string, count=0, flags=0)
# 在一个字符串中替换所有匹配正则表达式的字串，返回替换后的字符串
# repl: 替换匹配字符串的字符串
# count：匹配的最大替换次数
# '''
# #
# ls = re.sub(r'[1-9]\d{5}', ':zipcode', 'BIT100081 TSU100084')
# print(ls)
