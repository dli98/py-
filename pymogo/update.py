# 想一个数据库添加一个新的字段
from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017)
db = client['text']  # 数据库名字

# -----------------Inserting a Document---------------------#
db.inventory.insert_many([
    {'item': "canvas", 'qty': 100, 'size': {'h': 28, 'w': 35.5, 'uom': "cm"}, 'status': "A"},
    {'item': "journal", 'qty': 25, 'size': {'h': 14, 'w': 21, 'uom': "cm"}, 'status': "A"},
    {'item': "mat", 'qty': 85, 'size': {'h': 27.9, 'w': 35.5, 'uom': "cm"}, 'status': "A"},
    {'item': "mousepad", 'qty': 25, 'size': {'h': 19, 'w': 22.85, 'uom': "cm"}, 'status': "P"},
    {'item': "notebook", 'qty': 50, 'size': {'h': 8.5, 'w': 11, 'uom': "in"}, 'status': "P"},
    {'item': "paper", 'qty': 100, 'size': {'h': 8.5, 'w': 11, 'uom': "in"}, 'status': "D"},
    {'item': "planner", 'qty': 75, 'size': {'h': 22.85, 'w': 30, 'uom': "cm"}, 'status': "D"},
    {'item': "postcard", 'qty': 45, 'size': {'h': 10, 'w': 15.25, 'uom': "cm"}, 'status': "A"},
    {'item': "sketchbook", 'qty': 80, 'size': {'h': 14, 'w': 21, 'uom': "cm"}, 'status': "A"},
    {'item': "sketch pad", 'qty': 95, 'size': {'h': 22.85, 'w': 30.5, 'uom': "cm"}, 'status': "A"}
])

# db['inventory'].update_one({'item': 'paper'},
#                            {'$set': {'size.uom': 'cm', 'status': 'p'},
#                             '$currentDate': {'lastModified': True}})
#
# db['inventory'].update_many({'qty': {'$lt': 50}},
#                             {'$set': {'size.uom': 'in', 'status': 'p'},
#                              '$currentDate': {'lastModified': True}})


# $addToSet：向数组中添加元素，若数组本身含有该元素，则不添加，否则，添加，这样就避免了数组中的元素重复现象；
# $push：向数组尾部添加元素，但它不管数组中有没有该元素，都会添加
db['inventory'].update({'item': 'canvas'},
                            {'$addToSet': {'comments': {'name': 456, 'status': 'p'}},
                             '$currentDate': {'lastModified': True}}, True)

db['inventory'].update({'item': 'canvas'},
                            {'$addToSet': {'comments': {'name': 456, 'status': 'p'}},
                             '$currentDate': {'lastModified': True}}, True)

db['inventory'].update({'item': 'canvas'},
                            {'$push': {'comments': {'name': 456, 'status': 'p'}},
                             '$currentDate': {'lastModified': True}}, True)
# replace

# db['inventory'].replace_one(
#     {'item': "paper"},
#     {'item': "paper", 'instock': [{'warehouse': "A", 'qty': 60}, {'warehouse': "B", 'qty': 40}]}
# )
# db['inventory'].update({'size.h': 30}, {'size': tmp}, True)
client.close()
