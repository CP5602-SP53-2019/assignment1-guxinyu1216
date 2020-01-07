import random
import time

lowerLimit = -13800
upperLimit = 96800
numOfValues = 80000
noDuplicates = True

def saveToFile(_randomData):
    file = open('TASK1_TESTBn.txt', 'w')
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