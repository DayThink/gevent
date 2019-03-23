import gevent


def test1():
    print 12
    gevent.sleep(0)
    print 34


def test2():
    print 56
    gevent.sleep(0)
    print 78


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(test1),
        gevent.spawn(test2),
    ])
