# -*- coding: utf-8 -*-
from gevent import monkey
import gevent
import requests
import time

monkey.patch_all()

# 利用monkey将同步阻塞的requests改为异步，只有将requests库阻塞式 改为 非阻塞，异步操作才能实现。
# gevent库中的猴子补丁能够修改标准库里面大部分的阻塞式系统调用，这样在不改变原有代码的
# 情况下，将应用的阻塞式方法，变成协程式的(异步)

def req(url):
    print(url)
    resp = requests.get(url)
    print(resp.status_code, url)


def synchronous_times(urls):
    """同步请求运行时间"""
    start = time.time()
    for url in urls:
        req(url)
    end = time.time()
    print('同步执行时间 {} s'.format(end - start))


def asynchronous_times(urls):
    """异步请求运行时间"""
    start = time.time()
    gevent.joinall([gevent.spawn(req, url) for url in urls])
    end = time.time()
    print('异步执行时间 {} s'.format(end - start))


urls = ['https://book.douban.com/tag/小说', 'https://book.douban.com/tag/科幻',
        'https://book.douban.com/tag/漫画', 'https://book.douban.com/tag/奇幻',
        'https://book.douban.com/tag/历史', 'https://book.douban.com/tag/经济学']

synchronous_times(urls)
asynchronous_times(urls)