# -*- coding: utf-8 -*-
from redis import Redis

# host 因为是本机连接所以是 127.0.0.1，如果是其他机器连接应该为 192.168.199.135
cache = Redis(host='127.0.0.1', port=6379, password='xy')

if __name__ == '__main__':

    # 字符串的操作
    # 添加一个值进去，并设置过期时间为 60s ，如果没有设置，默认过期时间是永久
    # cache.set('username','nana',ex='60')
    # cache.set('wangde', 'li')
    # print(cache.get('wangde'))
    # cache.delete('wangde')

    # 列表的操作
    # cache.lpush('language','java')
    # cache.lpush('language','php')
    # cache.lpush('language','python')
    # print(cache.lrange('language',0,-1))

    # 集合的操作
    # cache.sadd('team','li')
    # cache.sadd('team','jia')
    # cache.sadd('team','cheng')
    # print(cache.smembers('team'))

    # 哈希的操作
    # cache.hset('runner','acsi','gel')
    # cache.hset('runner','saucony','shadow')
    # cache.hset('runner','puma','r698')
    # print(cache.hgetall('runner'))

    # 事务的操作
    # 把这些命令绑定到 pip 上面
    # pip = cache.pipeline()
    # pip.set('username','hani')
    # pip.set('usename','daling')
    # pip.execute()
    # print(cache.get('username'))

    # 发布与订阅功能
    # 举例（异步发送邮件的功能）：利用 redis 的发布与订阅功能来实现异步邮件发送
    # 我只要去发布一个信号，你订阅到这个信号以后，就可以去发送邮件了，发布方就不需要去等待邮件发送的结果
    # 分两个文件来实现，这边是订阅的功能

    ps = cache.pubsub()
    ps.subscribe('email')
    # 一直阻塞，循环进行监听
    while True:
        # ps.listen() 返回的是一个生成器，所以要进行遍历
        for item in ps.listen():
            if item['type'] == 'message':
                data = item['data']
                print(data)












