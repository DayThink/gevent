from greenlet import greenlet


def test1():
    print 12
    y = gr2.switch(56)
    print y


def test2(x):
    print x
    gr1.switch(34)
    print 78


if __name__ == '__main__':
    gr1 = greenlet(test1)
    gr2 = greenlet(test2)
    gr1.switch()