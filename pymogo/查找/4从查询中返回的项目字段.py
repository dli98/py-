from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017)
db = client['text']  # 数据库名字

db['inventory'].insert_many([
    {'item': "journal", 'status': "A", 'size': {'h': 14, 'w': 21, 'uom': "cm"},
     'instock': [{'warehouse': "A", 'qty': 5}]},
    {'item': "notebook", 'status': "A", 'size': {'h': 8.5, 'w': 11, 'uom': "in"},
     'instock': [{'warehouse': "C", 'qty': 5}]},
    {'item': "paper", 'status': "D", 'size': {'h': 8.5, 'w': 11, 'uom': "in"},
     'instock': [{'warehouse': "A", 'qty': 60}]},
    {'item': "planner", 'status': "D", 'size': {'h': 22.85, 'w': 30, 'uom': "cm"},
     'instock': [{'warehouse': "A", 'qty': 40}]},
    {'item': "postcard", 'status': "A", 'size': {'h': 10, 'w': 15.25, 'uom': "cm"},
     'instock': [{'warehouse': "B", 'qty': 15}, {'warehouse': "C", 'qty': 35}]}
])

#  结果中只显示item, status 和 _id（默认）
print(list(db['inventory'].find({'status': 'A'}, {'item': 1, 'status': 1})))

# Suppress _id Field
print(list(db['inventory'].find({'status': 'A'}, {'item': 1, 'status': 1, '_id': 0})))

# Return All But the Excluded Fields
print(list(db['inventory'].find({'status': 'A'}, {'status': 0, 'instock': 0})))

# Return Specific Fields in Embedded Documents
print(list(db['inventory'].find({'status': 'A'}, {'item': 1, 'status': 1, "size.uom": 1})))

# Suppress Specific Fields in Embedded Documents
print(list(db['inventory'].find({'status': 'A'}, {"size.uom": 0})))

# Projection on Embedded Documents in an Array
print(list(db['inventory'].find({'status': 'A'}, {'item': 1, 'status': 1, "instock.qty": 1})))

# Project Specific Array Elements in the Returned Array
# The following example uses the $slice projection operator to return the last element in the instock array
print(list(db['inventory'].find({'status': 'A'}, {'item': 1, 'status': 1, "instock": {'$slice': 1}})))

