class pool(object):

    def __init__(self,x1,x2,y):
        self.x1 = int(x1)
        self.x2 = int(x2)
        self.y = int(y)
    
    def __str__(self):
        return "(%s,%s,%s)"%(self.x1,self.x2,self.y)

class line(object):
    
    def __init__(self,m,b):
        self.m = m
        self.b = b
    
    def __str__(self):
        return "y = (%s)x + %s"%(self.m,self.b)

def getAllLines(fst,snd):
    lineList = []
    delY = snd.y - fst.y
    #get all possibilities of delta x
    for i in range (fst.x1, fst.x2+1):
        for e in range (snd.x1,snd.x2+1):
            delX = e-i
            #get m
            if delX ==0:
                m = 0
            else:
                m = delY / delX
            #use the first line to get b
            b = fst.y - m * i # i is x of first line
            lineEq = line(m,b)
            lineList.append(lineEq)
    return lineList

def checkScore(line,field):
    score = 0
    for f in range(0,len(field)):
        if line.m == 0:
            checkX = field[f].y - line.b
        else:
            checkX = (field[f].y - line.b)/ line.m
        if checkX >= field[f].x1 and checkX <= field[f].x2:
            score += field[f].x2 - field[f].x1

    return score        

class lineScore(object):
    lineValues = []
    
    def addLine(self,lst):
        self.lineValues.append(lst)
    
    def getHighScore(self):
        maximum = self.lineValues[0]
        for g in range(0,len(self.lineValues)):
            if self.lineValues[g][1] > maximum[1]:
                maximum = self.lineValues[g]
        return maximum

numPool = input("Please enter the number of oil repositories")
numPool = int(numPool)

#list of all the possible pair of repositories
fOne = []
for i in range(0,numPool):
    x1,x2,y = input("please enter the detail of pool %s, separated by space"%(i+1)).split()
    oilRepo = pool(x1,x2,y)
    fOne.append(oilRepo)

#for all the possible line 
allLine = []
#for each of the pair of repositories, get lines


for p in range(0,len(fOne)):
    for q in range(p+1,len(fOne)):
        fst = fOne[p]
        snd = fOne[q]
        
        
        tempList = getAllLines(fst,snd)
        allLine = []+tempList


allTheLine = lineScore()

for e in range(0,len(allLine)):
    quickList = [allLine[e], checkScore(allLine[e],fOne)]
    print(quickList[0]," ",quickList[1])
    allTheLine.addLine(quickList)

fEquation = allTheLine.getHighScore()
print("The equation of the line is :", fEquation[0])
print("the total amount of oil obtained: ", fEquation[1])




