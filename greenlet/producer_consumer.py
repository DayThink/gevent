from greenlet import greenlet

def consumer():
    last = ''
    while True:
        receival = pro.switch(last)
        if receival is not None:
            print 'Consume %s' % receival
            last = receival

def producer(n):
    con.switch()
    x = 0
    while x < n:
        x += 1
        print 'Produce %s' % x
        last = con.switch(x)

pro = greenlet(producer)
con = greenlet(consumer)
pro.switch(5)
