# -*- coding =utf-8 -*-
# @Time : 2020/12/28 9:21
# @Author : 陈文龙
# @File : parse_content.py
# @Software : PyCharm
# 说明：本文件用于打开35seyes3某特定小说页面用于爬取的方式
import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print('未成功返回html')
        return None


def parse_title(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.body.find(attrs='page_title').string
    print(title)
    return title.strip()


def parse_content(html):
    soup = BeautifulSoup(html, 'lxml')
    content = soup.body.find(attrs='content').find_all(name='p')
    for item in content:
        yield item.text


def main(url):
    html = get_html(url)
    title = parse_title(html)
    if '/'or'*' in title:
        title = title.replace('*', '或')
        title = title.replace('/', '或')
    f = open('' + title + '.txt', 'w', encoding='utf-8')  # 注意路径名字
    for i in parse_content(html):
        f.write(i + '\n')
    f.close()


