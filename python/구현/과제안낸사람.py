import sys

nList = list()
cList = list()
ansList = list()
k = 0

cList = [i for i in range(1, 31)]

for i in range(0, 28):
    nList.append(int(sys.stdin.readline()[:-1]))

nList = sorted(nList)
nList.append(0)
nList.append(0)
for i in cList:
    if i != nList[k]:
        nList.insert(i-1, 0)
        ansList.append(i)
    k+=1
        

for i in ansList:
    print(i)
