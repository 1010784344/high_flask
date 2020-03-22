# -*- coding: utf-8 -*-
import os
# 配置 ueditor 的本地上传路径
UEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'images')


# 配置 ueditor 的七牛上传路径
UEDITOR_UPLOAD_TO_QINIU = True
UEDITOR_QINIU_ACCESS_KEY = "PE4avHSNHAKI91mKjk8l7g-DhTQM9KSoxesVf9V3"
UEDITOR_QINIU_SECRET_KEY = "nMi3pP0nOEGX2OaC2KiY972UGFZ27wSiWM5qMLFO"
UEDITOR_QINIU_BUCKET_NAME = "dashu666"
UEDITOR_QINIU_DOMAIN = "http://q7bncq283.bkt.clouddn.com/"


if __name__ == '__main__':
    print
    1