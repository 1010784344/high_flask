# -*- coding: UTF-8 -*-
from flask import g




def log_a():
    print('This is log_a: %s'%g.username)

def log_b():
    print('This is log_b: %s'%g.username)

def log_c():
    print('This is log_c: %s'%g.username)







