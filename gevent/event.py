#coding:utf8
import gevent
from gevent.event import Event, AsyncResult

evt = Event()
aevt = AsyncResult()

def setter():
    # 3秒后唤醒所有在evt上等待的协程
    print 'Wait for me'
    gevent.sleep(3)
    print "Ok, I'm done"
    # evt.set()  # 唤醒
    aevt.set('Hello!')  # 唤醒，并传递消息

def waiter():
    print "I'll wait for you"
    # evt.wait()  # 等待
    # print 'Finish waiting'
    message = aevt.get()  # 等待，并在唤醒时获取消息
    print 'Got wake up message: %s' % message

gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
    gevent.spawn(waiter)
])