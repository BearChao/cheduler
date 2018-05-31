# coding=utf-8
import time
import requests
from bs4 import BeautifulSoup

def get_time():
    return time.strftime('%Y年%m月%d日 %H:%M ',time.localtime(time.time()))

#获得soup对象
def get_soup(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    try:
        html = requests.get(url, headers=headers)
        html = html.content.decode()
    except:
        return None
    return BeautifulSoup(html,'html.parser')