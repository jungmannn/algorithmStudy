# 첫번째 Math - 골드바흐의 추측
# 문제
# 1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.

# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
# 예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다. 또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.

# 이 추측은 아직도 해결되지 않은 문제이다.

# 백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.

# 입력
# 입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다. 테스트 케이스의 개수는 100,000개를 넘지 않는다.

# 각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다. (6 ≤ n ≤ 1000000)

# 입력의 마지막 줄에는 0이 하나 주어진다.

# 출력
# 각 테스트 케이스에 대해서, n = a + b 형태로 출력한다. 이때, a와 b는 홀수 소수이다. 숫자와 연산자는 공백 하나로 구분되어져 있다. 만약, n을 만들 수 있는 방법이 여러 가지라면, b-a가 가장 큰 것을 출력한다. 또, 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는 "Goldbach's conjecture is wrong."을 출력한다.

# 내 생각대로의 풀이
# 1. 에라토스테네스의 체 알고리즘을 사용해서 입력받은 수 보다 작은 소수를 모두 찾는다.
# 2. 소수의 리스트 n개부터 k까지의 합의 조합을 찾는데 k -> n순으로 진행해서 입력 받은 수와 동일한 합의 조합이 나오면 반복을 멈춘다.
# 3. b가 큰 순으로 더했기 때문에 맨 처음 나오는 조합이 해당 문제의 답이다.
import math

tList = list()
subList = list()
primeList = list()
while True:
    num = int(input())
    if num == 0:
        break
    tList.append(num)

print(tList)

for i in range(0, len(tList)):
    for k in range(1, tList[i] + 1):
        if (k == 2) or (k == 3) or (k == 5) or ((k != 1) and ( k % 2 != 0 ) and ( k % 3 != 0 ) and ( k % 5 != 0 )):
            subList.append(k)
    subList.reverse()
    primeList.append(subList)
    subList = []
    print(primeList)

for i in range(0, len(primeList)):
    # print(primeList[i])
    for j in range(0, len(primeList[i])):
        # print(primeList[i][j])
        for k in range(1, len(primeList[i]) - j):
            if (primeList[i][j] + primeList[i][j + k]) == tList[i]:
                print('찾았습니다.')
                print('a는')
                print(primeList[i][j])
                print('b는')
                print(primeList[i][j + k])
                print('합은')
                print(tList[i])
                print(tList[i] , " = " , primeList[i][j + k] , " + " , primeList[i][j] )
            break

## 시도횟수 : 1