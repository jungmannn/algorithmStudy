# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.

import sys
sys.setrecursionlimit(100000)

n, m = list(map(int, sys.stdin.readline().split()))

adList = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
count = 0

for i in range(0, m):
    edge = list(map(int, sys.stdin.readline().split()))
    adList[edge[0]].append(edge[1])
    adList[edge[1]].append(edge[0])

def dfs(v):
    visited[v] = True
    for i in adList[v]:
        if not visited[i]:
            dfs(i)

for j in range(1, n+1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)