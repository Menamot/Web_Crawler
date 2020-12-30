# -*- coding =utf-8 -*-
# @Time : 2020/12/28 14:45
# @Author : 陈文龙
# @File : parse_tout.py
# @Software : PyCharm

import json
import parse_content as pc


file = open('35小说目录古典武侠.txt', 'r', encoding='utf-8')
data = []
for line in file.readlines():
    dic = json.loads(line)
    data.append(dic)
r = 4015
i = r
for item in range(i, len(data)-1):
    url = data[item]['链接']
    print(url)
    print(i)
    i = i+1
    pc.main(url)
file.close()
