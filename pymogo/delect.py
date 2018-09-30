from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017)
db = client['text']  # 数据库名字

db['inventory'].delete_one({})
# Delete operations do not drop indexes, even if deleting all documents from a collection
db['inventory'].delete_many({})

db['inventory'].remove()
client.close()