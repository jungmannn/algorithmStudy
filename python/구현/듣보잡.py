# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다.
# 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다.
# 이름은 띄어쓰기 없이 영어 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

# 출력
# 듣보잡의 수와 그 명단을 사전순으로 출력한다.

import sys

sList = list()
lList = list()
ansList = list()

sDict = dict()
lDict = dict()

n, m = list(map(int, sys.stdin.readline().split()))

for i in range(0, n):
    sList.append(sys.stdin.readline()[:-1])
for i in range(0, m):
    lList.append(sys.stdin.readline()[:-1])

for i in sList:
    sDict[i] = sDict.get(i, 0) + 1

for i in lList:
    lDict[i] = lDict.get(i, 0) + 1

if n > m:
    for x in lList:
        if sDict.get(x):
            sDict[x] -= 1
        else:
            continue
    ansList = [k for k, v in sDict.items() if v == 0]
else:
    for x in sList:
        if lDict.get(x):
            lDict[x] -= 1
        else:
            continue
    ansList = [k for k, v in lDict.items() if v == 0]


ansList = sorted(ansList)

print(len(ansList))
for i in ansList:
    print(i)

