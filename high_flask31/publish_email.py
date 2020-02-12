# -*- coding: utf-8 -*-
from redis import Redis

# host 因为是本机连接所以是 127.0.0.1，如果是其他机器连接应该为 192.168.199.135
cache = Redis(host='127.0.0.1', port=6379, password='xy')

if __name__ == '__main__':

    # 发布与订阅功能
    # 举例（异步发送邮件的功能）：利用 redis 的发布与订阅功能来实现异步邮件发送
    # 我只要去发布一个信号，你订阅到这个信号以后，就可以去发送邮件了，发布方就不需要去等待邮件发送的结果
    # 分两个文件来实现，这边是发布的功能

    for i in range(3):
        cache.publish('email','loveyou')