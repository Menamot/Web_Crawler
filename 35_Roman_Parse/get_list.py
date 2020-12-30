# -*- coding =utf-8 -*-
# @Time : 2020/12/28 8:50
# @Author : 陈文龙
# @File : get_list.py
# @Software : PyCharm

import requests
from bs4 import BeautifulSoup
import json


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        }
    response = requests.get(url, headers)
    if response.status_code == 200:
        return response.text
    return None


def parse_one_page(html):
    soup = BeautifulSoup(html, 'lxml')
    lis = soup.find(attrs='box list channel').find_all(name='li')
    for li in lis:
        yield {
            '书名': li.find(name='a').attrs['title'],
            '链接': str('http://www.35seye3.com' + str(li.find(name='a').attrs['href']))
        }


f = open('35小说目录古典武侠.txt', 'w', encoding='utf-8')
for i in range(600):
    url = 'http://www.35seye3.com/newslist/50/index-' + str(i) + '.html'
    html = get_html(url)
    for item in parse_one_page(html):
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
    print('已成功爬取第', i, '页目录')
f.close()
