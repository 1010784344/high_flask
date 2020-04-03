# -*- coding: UTF-8 -*-
from task import send_email



# 执行 main.py 来触发任务
if __name__ == '__main__':
    send_email.delay()


# 任务的真正执行在终端：celery -A task.celery --pool=eventlet worker --loglevel=info