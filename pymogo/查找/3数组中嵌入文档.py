from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017)
db = client['text']  # 数据库名字

# post_id = db['inventory'].insert_many(
#     [{'item': "canvas1", 'tags': [{'h': 28, 'uom': "in"}, {'h': 30, 'uom': "cm"}]},
#      {'item': "canvas2", 'tags': [{'h': 15}]},
#      {'item': "canvas3", 'tags': [{'h': 10, 'uom': "cm"}, {'h': 28, 'uom': "in"}]},
#      {'item': "canvas4", 'tags': [{'h': 10, 'uom': "cm"}, {'h': 30, 'uom': "cm"}]},
#      {'item': "canvas5", 'tags': [{'h': 28, 'uom': "cm"}, {'h': 30, 'uom': "cm"}]},
#      {'item': "canvas6", 'tags': [{'h': 30, 'uom': "out"}, {'h': 28, 'uom': "cm"}]},
#      ]
# )

# -------------嵌入数组------------------------#
# Equality matches on the whole embedded/nested document
# require an exact match of the specified document, including the field orde
# print(list(db['inventory'].find({'tags': {'h': 28, 'uom': 'in'}})))
# print(list(db['inventory'].find({'tags': {'uom': 'in', 'h': 28}})))

# 字段查询
# print(list(db['inventory'].find({'tags.0.uom': 'in'})))

# elemMatch  array文档至少一个满足 同一个元素中的键值组合
# print(list(db['inventory'].find({'tags': {'$elemMatch': {'uom': 'in', 'h': 28}}})))
# print(list(db['inventory'].find({'tags': {'$elemMatch': {'h': 28}}})))
print(list(db['inventory'].find({'tags': {'$elemMatch': {'h': {'$gt': 10, '$lte': 20}}}})))

# 例如，以下查询匹配文档，其中嵌套在tags数组中的任何文档的h字段大于11，
# 并且数组中的任何文档（但不一定是相同的嵌入文档）的h字段小于或等于20：
print(list(db['inventory'].find({'tags.h': {'$gt': 11, '$lte': 20}})))
client.close()
