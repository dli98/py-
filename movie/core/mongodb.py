import pymongo
from conf.setting import HOST, PORT, DB_NAME, COLLECTION_NAME

class MongoDB_Client:
    def __init__(self, host=HOST, port=PORT, db_name = DB_NAME, collection = COLLECTION_NAME):
        client = pymongo.MongoClient(host, port)
        self._db = client[db_name]  # 连接数据库
        self._colle = self._db[collection] # 连接要操作的集合

    def read_mongo(self, *args, **kwargs):
        cursor = self._colle.find(*args, **kwargs)
        print('数据读取成功')
        return cursor

    def save_to_mongo(self, result, id_):
        if self._colle.update({'id': result['id']}, {'$set': result}, True):
            print('存入MONGODB成功')
            return True
        return False
