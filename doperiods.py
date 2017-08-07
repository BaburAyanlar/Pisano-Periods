class PisanoS():
    def __init__(self, file):
        self.file = open(file, 'r')
        self.list = ((self.file.read()).split('\n'))
        self.length = len(self.list)
        

    def findPattern (self):
        counter = 0
        
        for i in range(0, self.length):    
            if (self.list[i] == '0' and self.list[i+1] == '1' and self.list[i+2] == '1'):
                    counter = counter +1
                    #print "count"
                    #continue
                    if (counter >= 2):
                        break
            else:
                continue
        self.period = i

    def listClose(self):
        self.file.close()
        
        
Fibstring = ""
for i in range (2,41):
    string = "ParseRem%s" %i
    Pis = PisanoS(string)
    Pis.findPattern()
    p = str(Pis.period)
    Fibstring += p
    Fibstring += "\n"
    Pis.listClose()

Periodlist = open("Periods.txt", 'w')
Periodlist.write(Fibstring)
Periodlist.close()

    
