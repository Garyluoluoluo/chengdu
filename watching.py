import urllib.request
import re
from bs4 import BeautifulSoup
import time
import requests
import json
from wxpy import *
import csv
from time import strftime

wechat = input('是否启用微信通知功能： Y/N ？')
if wechat == 'y' or wechat == 'Y':
	wechat = 1
else:
	wechat = 0

if wechat :

    watcher = input('请输入微信名称:' )  #需要通知的watcher 微信名
    bot = Bot()
    bot.enable_puid() #启用聊天对象的puis属性
    my_friend = bot.friends().search(watcher)[0]
sleeptime = 1800        # 单位为秒


url = 'http://www.cdfangxie.com/Infor/type/typeid/36.html'

def checkhouse(url):
    house_lis = []
    response = urllib.request.urlopen(url)
    code = response.getcode()
    html = response.read()
    mystr = html.decode("utf8")
    response.close()
    # print(mystr)
    soup = BeautifulSoup(mystr, "html.parser")
    for tag in soup.find_all("a",href=re.compile("Infor"),target="_blank"):
        house = tag.string.split("|")
        house_lis.append(house)
    return house_lis

if __name__ == '__main__':
    houselist1 = []
    i = 0
    while True:
        houselist2 = checkhouse(url)
        if houselist1 == houselist2:
            print('没有更新数据'+str(houselist2[0]))
            if wechat :
                my_friend.send('没有更新数据'+str(houselist2[0]))
        else:
            if i > 0 :
                print("新增楼盘>>>>"+ str(houselist2[0]))
                if wechat :
                    my_friend.send("新增楼盘>>>>"+ str(houselist2[0]))
            elif i == 0:
                print('启动成功，当前楼盘列表:'+str(houselist2))
                if wechat :
                    my_friend.send('启动成功，当前楼盘列表:'+str(houselist2))
        if i > 100:
            i = 1
        houselist1 = houselist2
        time.sleep(sleeptime)
        i += 1

