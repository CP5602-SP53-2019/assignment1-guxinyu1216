import random
import time

lowerLimit = -13800
upperLimit = 96800
numOfValues = 80000
noDuplicates = False

def saveToFile(_randomData):
    file = open('TASK2_TESTCn.txt', 'w')
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

def insertionSort(List): 
   for i in range(1,len(List)):
      current = List[i]
      j = i
      while j > 0 and List[j-1] > current:
         List[j] = List[j-1]
         j -= 1
         List[j] = current
   return List

start_time=time.time()
RawLis = rNGenerator(lowerLimit, upperLimit, numOfValues, noDuplicates)
PData = insertionSort(RawLis)
saveToFile(str(PData))
print("The generation takes {:.5f} seconds".format(time.time()-start_time))