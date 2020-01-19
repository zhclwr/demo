import json
import time

import requests

from domain import Proxy
from utils.httpUtil import get_user_agent
from utils.log import logger


def check_proxy(proxy: Proxy):
    """
    :param proxy:
    :return:
    """
    proxies = {
        'http': 'http://{}:{}'.format(proxy.ip, proxy.port),
        'https': 'https://{}:{}'.format(proxy.ip, proxy.port)
    }

    http, http_nick_type, http_speed = __check(proxies)
    https, https_nick_type, https_speed = __check(proxies)
    if http and https:
        proxy.protocol = 2
        proxy.nick_type = http_nick_type
        proxy.speed = http_speed
    elif http:
        proxy.protocol = 0
        proxy.nick_type = http_nick_type
        proxy.speed = http_speed
    elif https:
        proxy.protocol = 1
        proxy.nick_type = https_nick_type
        proxy.speed = https_speed
    else:
        proxy.protocol = -1
        proxy.nick_type = -1
        proxy.speed = -1
    return proxy


def check_origin(arr):
    first = arr[0]
    for i in arr[1:]:
        if first != i.lstrip():
            return 0
    return 2


def __check(proxies, isHttp=True):
    if isHttp:
        test_url = 'http://httpbin.org/get'
    else:
        test_url = 'https://httpbin.org/get'
    speed = -1
    nick_type = -1
    try:
        start = time.time()
        response = requests.get(test_url, headers=get_user_agent(), proxies=proxies, timeout=10)
        print(response.text)
        if response.ok:
            speed = round(time.time() - start, 2)
            dic = json.loads(response.text)
            origin = dic['origin']
            headers = dic['headers']
            proxy_connection = headers.get('Proxy-Connection', None)
            # 有多个ip
            if ',' in origin:
                arr = origin.split(',')
                # 有两个ip
                nick_type = check_origin(arr)
            elif proxy_connection:
                nick_type = 1
            else:
                nick_type = 2
            return True, nick_type, speed
        else:
            return False, nick_type, speed
    except Exception as e:
        logger.debug(e)
        return False, nick_type, speed


if __name__ == '__main__':
    p = check_proxy(Proxy('36.27.28.171', '9999'))
    print(p)
