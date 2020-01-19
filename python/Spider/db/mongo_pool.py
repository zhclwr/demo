from pymongo import MongoClient

from domain import Proxy
from setting import MONGO_URL, MONGO_DB, MONGO_TABLE
from utils.log import logger


class MongoPool(object):
    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self.proxies = self.client[MONGO_DB][MONGO_TABLE]

    def __del__(self):
        self.client.close()

    def insert_one(self, proxy: Proxy):
        count = self.proxies.count_documents({'_id': proxy.ip})
        if count == 0:
            dic = proxy.__dict__
            dic['_id'] = proxy.ip
            self.proxies.insert_one(dic)
            logger.info("ip: {} 插入成功".format(proxy.ip))
        else:
            logger.warning('ip: {} 已存在'.format(proxy.ip))

    def update_one(self, proxy: Proxy):
        self.proxies.update_one({'_id': proxy.ip}, {'$set': proxy.__dict__})
        logger.info("ip: {} 更新成功".format(proxy.ip))

    def delete_one(self, proxy:Proxy):
        self.proxies.delete_one({'_id': proxy.ip})
        logger.info("ip: {} 删除成功".format(proxy.ip))

    def find_all(self):
        for item in self.proxies.find():
            item.pop('_id')
            proxy = Proxy(**item)
            yield proxy


if __name__ == '__main__':
    proxy = Proxy("223.199.23.53", "9999")
    mongo = MongoPool()
    mongo.delete_one(proxy)
    for i in mongo.find_all():
        print(i)