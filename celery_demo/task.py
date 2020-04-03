# -*- coding: UTF-8 -*-
from celery import Celery
from time import sleep

# 初始化 celery 对象
celery = Celery('task',broker='redis://@127.0.0.1:6379/0',backend='redis://@127.0.0.1:6379/0')


# 定义一个任务
@celery.task
def send_email():
    print('邮件开始发送！')
    sleep(5)
    print('邮件发送成功！')

if __name__ == '__main__':
    pass