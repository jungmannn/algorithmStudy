# 첫번째 Math - 최대공약수 합
# 문제
# 양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 t (1 ≤ t ≤ 100)이 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있다. 각 테스트 케이스는 수의 개수 n (1 < n ≤ 100)가 주어지고, 다음에는 n개의 수가 주어진다. 입력으로 주어지는 수는 1000000을 넘지 않는다.

# 출력
# 각 테스트 케이스마다 가능한 모든 쌍의 GCD의 합을 출력한다.

tNum = int(input())
abList = list()
resultList = list()
sum = 0
for i in range(0, tNum):
    abList.append(input().split())

print(abList)

def gcdFunction(a, b):
    if b == 0:
        if a == 1:
            return 0
        else:
            return a
    else:
        return gcdFunction(b, a%b)

for i in range(0, tNum):
    for j in range(0, len(abList[i])):
        for k in range(1, len(abList[i]) - j):
            sum += gcdFunction(int(abList[i][j]), int(abList[i][j + k]))
    resultList.append(sum)
    sum = 0
for i in resultList:
    print(i)

# for i in range(0, tNum):
#     for j in range(0, len(abList[i])):
#         for k in range(1, len(abList[i]) + 1):
#             print(gcdFunction(abList[i][j], abList[i][j + k]))

# 0,1 + 0,2 + 0,3 + 0,4 + 1,2 + 1,3 + 1,4 + 2,3 + 2,4 + 3,4

# 0, 1, 2, 3, 4


# n , n + 1 // n, n + 2 // n, n + 3 // n, n + 4 => n ++, k--
# n, n + 1 // n, n + 2 // n, n + 3 => n++, k--
# n, n + 1 // n, n + 2 // n, n => n++, k--
# n, n + 1 // n, n + 2 // => end

## 시도횟수 : 1