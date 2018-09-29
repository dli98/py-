#  Query for Null or Missing Fields

from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017)
db = client['text']  # 数据库名字

# db['inventory'].insert_many([
#     {'_id': 1, 'item': None},
#     {'_id': 2}
# ])

# The { item : null } query matches documents
# that either contain the item field whose value is null or that do not contain the item field
print(list(db['inventory'].find({'item': None})))

#  only documents that contain the item field whose value is null
print(list(db['inventory'].find({'item': {'$type': 10}})))

# The { item : { $exists: false } } query matches documents that do not contain the item field:
print(list(db['inventory'].find({'item': {'$exists': True}})))
print(list(db['inventory'].find({'item': {'$exists': False}})))

client.close()