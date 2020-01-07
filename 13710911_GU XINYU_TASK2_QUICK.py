import random
import time

lowerLimit = -13800
upperLimit = 96800
numOfValues = 80000
noDuplicates = False

def saveToFile(_randomData):
    file = open('TASK2_TESTDn.txt', 'w')
    file.write(_randomData)

def rNGenerator(lowerLimit, upperLimit, numOfValues, noDuplicates):
    if noDuplicates == False:
        ranDataLis = []
        for i in range(numOfValues):
            data = random.randint(lowerLimit, upperLimit)
            ranDataLis.append(data)
        return ranDataLis
    else:
        ranDataLis = []
        while len(ranDataLis) < numOfValues:
            data = random.randint(lowerLimit, upperLimit)
            if data in ranDataLis:
                pass
            else:
                ranDataLis.append(data)
        return ranDataLis

def quickSort(List): 
    if len(List)<2:
        return List
    mid = List.pop(0)
    left = []
    right = []
    for i in List:
        if i > mid:
            right.append(i)
        else:
            left.append(i)
    return quickSort(left) + [mid] + quickSort(right)

start_time=time.time()
RawLis = rNGenerator(lowerLimit, upperLimit, numOfValues, noDuplicates)
PData = quickSort(RawLis)
saveToFile(str(PData))
print("The generation takes {:.5f} seconds".format(time.time()-start_time))