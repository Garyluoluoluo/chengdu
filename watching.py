import urllib.request
import re
from bs4 import BeautifulSoup
import time

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
            print('没有更新数据'+str(houselist1[0]))
        else:
            if i > 0 :
                print("新增楼盘>>>>"+ str(houselist2[0]))
        if i > 100:
            i = 1
        houselist1 = houselist2
        time.sleep(600)
        i += 1

