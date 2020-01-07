import random
import time

lowerLimit = -35500
upperLimit = 36600
numOfValues = 50000
noDuplicates = True

def saveToFile(_randomData):
    file = open('TASK1_TESTB1.txt', 'w')
    file.write(_randomData)

def rNGenerator(lowerLimit, upperLimit, numOfValues, noDuplicates):
    if noDuplicates == False:
        randomData = ""
        for i in range(numOfValues):
            data = random.randint(lowerLimit, upperLimit)
            randomData += str(data) + '\n'
        saveToFile(randomData)
    else:
        ranDataLis = []
        while len(ranDataLis) < numOfValues:
            data = random.randint(lowerLimit, upperLimit)
            if data in ranDataLis:
                pass
            else:
                ranDataLis.append(data)
        saveToFile(str(ranDataLis))

start_time=time.time()
rNGenerator(lowerLimit, upperLimit, numOfValues, noDuplicates)
print("The generation takes {:.5f} seconds".format(time.time()-start_time))