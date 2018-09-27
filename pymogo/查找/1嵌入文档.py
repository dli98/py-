from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017)
db = client['text']  # 数据库名字

post_id = db['inventory'].insert_many(
    [{'item': "canvas1", 'qty': 20, 'tags': ["blank", 'red', 'blue'], 'size': {'h': 28, 'w': 35.5, 'uom': "cm"}},
     {'item': "canvas2", 'qty': 100, 'tags': ["red", 'blank'], 'size': {'h': 8.5, 'w': 11.5, 'uom': "in"}},
     {'item': "canvas3", 'qty': 60, 'tags': ["blank", 'red'], 'size': {'h': 8.5, 'w': 11.5, 'uom': "in"}},
     {'item': "canvas4", 'qty': 45, 'tags': ["blank", 'red'], 'size': {'h': 30, 'w': 20.5, 'uom': "cm"}},
     {'item': "canvas5", 'qty': 30, 'tags': ['blue'], 'size': {'h': 30, 'w': 20.5, 'uom': "cm"}}
     ]
)

# --------------嵌入文档 ----------------------#
print(list(db['inventory'].find({'size.h': 28})))  # 查询嵌入文档里面的字段，用.
# 字典里面的字段（field）必须完全匹配 order 顺序不能乱
print(list(db['inventory'].find({'size': {'h': 28, 'w': 35.5, 'uom': "cm"}})))
print(list(db['inventory'].find({'size': {'w': 35.5, 'uom': "cm", 'h': 28}})))
print(list(db['inventory'].find({'size': {'w': 35.5, 'uom': "cm"}})))

client.close()
