from os.path import exists
FibSeries = open("FibSeries.txt", 'w')
if (exists("FibSeries.txt") == 1) :
    a = 0
    b = 1
    #print "0"
    FibSeries.write("0\n")
    for i in range (0,10000):
        pb = "%s\n"%(str(b))
        FibSeries.write(pb)
        #print '%d '%b
        olda = a
        oldb = b
        b = a + b
        a = oldb
Fibseries.close()
else : print "File Creation Failed"
