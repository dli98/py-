from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017)
db = client['text']  # 数据库名字

# -----------------Inserting a Document---------------------#
post_id = db['inventory'].insert_one(
    {'item': "canvas", 'qty': 100, 'tags': ["cotton"], 'size': {'h': 28, 'w': 35.5, 'uom': "cm"}}
)
print(post_id)

# ------------显示这个数据库下的所有几个名字-------------------#
print(db.collection_names())

# --------Getting a Single Document With find_one()--------#

print(db['inventory'].find_one())
print(db['inventory'].find_one({'item': 'canvas'}))

# A common task in web applications is to get an ObjectId from the
# request URL and find the matching document.
# It’s necessary in this case to convert the ObjectId from a string before passing it to find_one:
#


# -----------------Bulk insert ---------------------#
post_id = db['inventory'].insert_many(
    [{'item': "canvas1", 'qty': 100, 'tags': ["cotton"], 'size': {'h': 28, 'w': 35.5, 'uom': "cm"}},
     {'item': "canvas2", 'qty': 100, 'tags': ["cotton"], 'size': {'h': 28, 'w': 35.5, 'uom': "cm"}}
     ]
)
print(post_id)
print(post_id.inserted_ids)
client.close()

# ------Querying for More Than One Document----------#
# --------------------find()-------------------------#



# -------------------Aggregation Framework-----------#
result = db['aggregation'].insert_many(
    [{'x': "1", 'tags': ["cat", 'dog', 'mouse']},
     {'x': "2", 'tags': ["cat", 'dog', 'mouse']},
     {'x': "3", 'tags': ["cat", 'dog', 'mouse']},
     {'x': "4", 'tags': ['dog']},
     {'x': "5", 'tags': ['pig']},
     ]
)

from bson.son import SON
pipeline = [
    {'$unwind': '$tags'},
    {'$group': {'_id': '$tags', 'count': {'$sum': 1}}},
    {'$sort': SON([('count', -1), ('_id', -1)])},
]
print(list(db['aggregation'].aggregate(pipeline)))

db['aggregation'].map_reduce()