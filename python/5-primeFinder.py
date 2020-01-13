# 첫번째 Math - 소수 찾기
# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.
count = 0
nNum = int(input())
nList = list(map(int, input().split()))
if len(nList) > nNum:
    print('개수 초과')

for i in range(0, nNum):
    if (nList[i] == 2) or (nList[i] == 3) or ((nList[i] != 1) and ( nList[i] % 2 != 0 ) and ( nList[i] % 3 != 0 )):
        count += 1
print(count)
## 시도횟수 : 2 파이썬이라서 틀림