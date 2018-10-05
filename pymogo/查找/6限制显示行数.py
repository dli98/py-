from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017)
db = client['text']  # 数据库名字


cursor = db['inventory'].find({}).limit(2)
for i in cursor:
    print(i)


cursor = db['inventory'].find({}).limit(2).skip(2)
for i in cursor:
    print(i)


# cursor = db['inventory'].find({'$or': [{'qty': {'$gt': 95}}, {'qty': {'$lt': 30}}]})
# cursor = db['inventory'].find({'qty': {'$gt': 80}})
# for i in cursor:
#     print(i)