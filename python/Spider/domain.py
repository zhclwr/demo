from setting import *


class Proxy(object):
    def __init__(self, ip, port, protocol=-1, nick_type=-1, speed=-1, area=None, score=MAX_SCORE, disable_domains=[]):
        self.ip = ip
        self.port = port
        # 代理IP支持的协议类型，http:0 https:1 both:2
        self.protocol = protocol
        # 匿名程度 透明：0  匿名：1 高匿: 2
        self.nick_type = nick_type
        # 响应速度 单位s
        self.speed = speed
        # 所在地区
        self.area = area
        # 得分
        self.score = score
        # 不可用域名列表
        self.disable_domains = disable_domains

    def __str__(self):
        return str(self.__dict__)