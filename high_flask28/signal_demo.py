# -*- coding: UTF-8 -*-
import os
from flask import g,request
from blinker import Namespace
from datetime import datetime


# 获取当前目录
currentdir = os.path.dirname(__file__)


# 定义命名空间
wangzhespace = Namespace()
# 定义信号
nake_signal = wangzhespace.signal('libai')



# 定义信号执行函数
def loulou(sender):
    user = g.user
    print(user)
    now = datetime.now()
    IP = request.remote_addr

    loginline = '%s * %s * %s *\n' % (now, user, IP)
    print(loginline)
    with open(currentdir + '\login_log.txt','a') as fp:
        print(currentdir)
        fp.write(loginline)


# 监听信号
nake_signal.connect(loulou)



