#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/9 下午11:19
# @Author  : Bear Chao
# @Site    : http://blog.nickzy.com
# @File    : ultraflightMP.py
# @Software: PyCharm

import requests
url = 'http://139.199.212.48:8080/'

def check_ufmp_status():
    r = requests.get(url)
    if r.status_code == 200:
        return True
    else:
        return False
