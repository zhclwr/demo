# ip最大得分
import logging

MAX_SCORE = 50

LOG_LEVEL = logging.DEBUG
LOG_FMT = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'
LOG_DATE_FMT = '%Y-%m-%d %H:%M:%S'
LOG_FILENAME = 'log.log'

MONGO_URL = 'mongodb://127.0.0.1:27017'
MONGO_DB = 'proxies'
MONGO_TABLE = 'proxies'
