# 두 번째 브루트 포스 - 테트로미노
import sys

n = m = 0
arr = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
maxVal = 0

def dfs(x, y, visited, count, sumVal):
    global maxVal

    if count == 4:
        if maxVal < sumVal:
            maxVal = sumVal
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < m:
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                dfs(nx, ny, visited, count + 1, sumVal + arr[nx][ny])
                visited[nx][ny] = False

def oh(x, y):
    global maxVal
    sumVal = arr[x][y]

    if x == 0:
        if y == 0 or y == m-1:
            return
    elif x == n-1:
        if y == 0 or y == m-1:
            return
    if x == 0:
        sumVal += arr[x+1][y] + arr[x][y-1] + arr[x][y+1]
    elif x == n-1: 
        sumVal += arr[x-1][y] + arr[x][y-1] + arr[x][y+1]    
    elif y == 0:
        sumVal += arr[x][y+1] + arr[x-1][y] + arr[x+1][y]
    elif y == m-1:
        sumVal += arr[x][y-1] + arr[x-1][y] + arr[x+1][y]
    else:  
        sumlist = []
        sumlist.append(sumVal + arr[x+1][y] + arr[x][y-1] + arr[x][y+1])
        sumlist.append(sumVal + arr[x-1][y] + arr[x][y-1] + arr[x][y+1])
        sumlist.append(sumVal + arr[x][y+1] + arr[x-1][y] + arr[x+1][y])
        sumlist.append(sumVal + arr[x][y-1] + arr[x-1][y] + arr[x+1][y])
        sumVal = max(sumlist)

    if maxVal < sumVal:
        maxVal = sumVal

def solve():
    visited = [[False]*m for i in range(n)]

    for i in range(n):
        for j in range(m):
            oh(i, j)
            visited[i][j] = True
            dfs(i, j, visited, 1, arr[i][j])
            visited[i][j] = False
    
if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
 
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
        
    solve()
    print(maxVal)