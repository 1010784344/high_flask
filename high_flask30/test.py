# -*- coding: utf-8 -*-
import memcache

mc = memcache.Client(['127.0.0.1:11211'],debug=True)

if __name__ == '__main__':

    # 设置一个或多个值
    # mc.set('username','lirui',time=120)
    # mc.set_multi({'user':'li','name':'rui'},time=120)

    # 获取对应的值
    # username = mc.get('username')
    # print(username)

    # 删除某一个值
    # mc.delete('username')

    # 获取对应的值
    # username = mc.get('username')
    # print(username)

    # 增加
    mc.incr('age',delta=2)
    age = mc.get('age')
    print(age)

    # 减少
    mc.decr('age',delta=2)
    age = mc.get('age')
    print(age)



