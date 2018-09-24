import pymongo

MONGO_URL = 'localhost'
MONGO_DB = 'mafengwo'

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def save_to_mongo(name, item):
    db[name].update({'provice_id': item['provice_id']}, {'$set': item}, True)


def city_info_to_mongo(name, item):
    db[name].update({'city_name': item['city_name']}, {'$set': item}, True)
