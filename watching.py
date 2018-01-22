import urllib.request
import re
import http.cookiejar
from bs4 import BeautifulSoup
import time
url = 'http://www.cdfangxie.com/Infor/type/typeid/36.html'
#直接通过url来获取网页数据  


# for child in soup.descendants:
#     print(child)
#
# for string in soup.stripped_strings:
#     print(repr(string))
#print(soup.find_all("a", target="_blank"))

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
houselist1 = []
i = 0
while True:
    houselist2 = checkhouse(url)


    if houselist1 == houselist2:
        print('没有更新数据')
    else:
        if i > 0 :
            print("新增楼盘>>>>"+ str(houselist2[0]))
    if i > 100:
        i = 1
    houselist1 = houselist2
    time.sleep(2)
    i += 1
    #print(house_dic)
#print(soup.div)

# while True:
#     x = input( "查询当前编号：" )
#     if int(x) in range(len(house_lis)):
#        print(house_lis[int(x)])
#     else:
#         x = input("请输入正确编号")

