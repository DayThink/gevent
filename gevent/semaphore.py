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