from pymongo import MongoClient
import pymongo
client = MongoClient(host='localhost', port=27017)
db = client['text']  # 数据库名字

result = db.profiles.create_index([('user_id', pymongo.ASCENDING)], unique=True)

# The index prevents us from inserting a document whose user_id is already in the collection
user_profiles = [
    {'user_id': 222, 'name': 'Luke'},
    {'user_id': 252, 'name': 'Ziltoid'}]
result = db.profiles.insert_many(user_profiles)
client.close()