#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/28 下午10:57
# @Author  : Bear Chao
# @Site    : http://blog.nickzy.com
# @File    : run.py
# @Software: PyCharm

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from pushover import Client

from tasks.qqvideo import QQVideoData
from tasks.youku import YoukuData

client = Client("umfy11bfzx28a7hx4jswf7i71mg4te", api_token="a4rvvdmwnt8sobjif8rborp64uhrnf")
# client.send_message(message="测试内容\nceshineirong<br><H1>word</H1>",
#                     html=1,
#                     title="测试HTML_image",
#                     url="https://pushover.net/api#html",
#                     url_title="api地址",
#                     attachment=("image.jpg", open("/Users/zynick/Pictures/IMG_856F4CDA6635-1.jpeg", "rb"), "image/jpeg"))

# 输出时间
def job():
    v = YoukuData()
    client.send_message(title="优酷视频播放量",
                        message="总播放量："+v.get_play_num()+"\n"+v.get_play_num_more()
                        )
    s = QQVideoData()
    client.send_message(title="腾讯视频播放量",
                        message="总播放量："+s.get_play_num()+"\n"+s.get_play_num_more()
                        )
job()
# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', day_of_week='1', hour=7, minute=30)
scheduler.start()