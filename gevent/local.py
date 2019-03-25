import gevent
from gevent.local import local

data = local()

def f1():
    data.x = 1
    print 'f1 = ', data.x
    gevent.sleep()
    print 'f1 = ', data.x

def f2():
    try:
        data.x = 2
        print 'f2 = ', data.x
    except AttributeError:
        print 'x is not visible'

gevent.joinall([
    gevent.spawn(f1),
    gevent.spawn(f2)
])