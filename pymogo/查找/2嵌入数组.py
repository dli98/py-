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

# -------------嵌入数组------------------------#
print(list(db['inventory'].find({'tags': ['blue']})))  # 完全匹配
print(list(db['inventory'].find({'tags': ['red', 'blank']})))

# ---只要拥有red和blank即可，不必在意顺序---------#
# all用在array上，不能在嵌入文档
print(list(db['inventory'].find({'tags': {'$all': ['red', 'blank']}})))

# -----------tags字段至少包含一个blue-----------#
print(list(db['inventory'].find({'tags': 'blue'})))


# -----------tags字段的大小 -----------------#
print(list(db['inventory'].find({'tags': {'$size': 3}})))

# -------------.
print(list(db['inventory2'].find({'tags.0': 'blue'})))
