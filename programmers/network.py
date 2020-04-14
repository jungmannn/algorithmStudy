from queue import Queue
n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

def solution(n, computers):
    answer = 0
    visit = [0] * n
    bfs = Queue()
    bfs.put(0)

    while 0 in visit:
        bfs.put(visit.index(0))
        while bfs.qsize() > 0:
            node = bfs.get()
            visit[node] = 1
            for i in range(n):
                if visit[i] == 0 and computers[node][i] == 1:
                    bfs.put(i)
        answer += 1
    return answer

print(solution(n, computers))



