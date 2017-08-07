Fibdata = open("FibSeries.txt", 'r')
Fibstring = ""
Fiblist = []
Fibremlist = []
Fibremstring = ""
if Fibdata:
    Fibstring = Fibdata.read()
    Fiblist = Fibstring.split('\n')
    for i in range (2,41):
        index = str(i)
        for j in range (0,10001):
            element = int(Fiblist[j])%i
            Fibremlist.append(element)
            stringelement = str(element)
            Fibremstring += "%s\n"%stringelement
        RemFileName = "C:\Users\Babs\\newfolds\PisanoSeries\ParseFiles\ParseRem%s"%index
        Newfile = open(RemFileName, 'w')
        Newfile.write(Fibremstring)
        Newfile.close()
        Fibremstring = ""
