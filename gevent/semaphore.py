# -*- coding: utf-8 -*-
import gevent
from gevent.lock import BoundedSemaphore

sem = BoundedSemaphore(2)


def worker(n):
    sem.acquire()
    print('Worker %i acquired semaphore' % n)
    gevent.sleep(0)
    sem.release()
    print('Worker %i released semaphore' % n)


gevent.joinall([gevent.spawn(worker, i) for i in xrange(0, 6)])

print u'========分割线========'

from gevent import sleep
from gevent.pool import Pool

def worker1(n):
    sem.acquire()
    print('Worker %i acquired semaphore' % n)
    sleep(0)
    sem.release()
    print('Worker %i released semaphore' % n)

def worker2(n):
    with sem:
        print('Worker %i acquired semaphore' % n)
        sleep(0)
    print('Worker %i released semaphore' % n)

pool = Pool()
pool.map(worker1, xrange(0,2))
pool.map(worker2, xrange(3,6))