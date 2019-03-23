from greenlet import greenlet, GreenletExit 

def test1(): 
    print 12
    gr2.throw(NameError) 
    #gr2.throw(GreenletExit)
    try:
        gr2.switch()
    except NameError:
        print 90
    print 34

def test2(): 
    print 56 
    #raise NameError
    #raise GreenletExit
    print 78 

gr1 = greenlet(test1) 
gr2 = greenlet(test2, gr1)
gr1.switch()
