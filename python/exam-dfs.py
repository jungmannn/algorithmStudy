# dfs example

vertextList = ['0', '1', '2', '3', '4', '5', '6']

edgeList = [(0 , 1), (0,2), (1, 0), (1, 3), (2,0), (2, 4), (2, 5), (3, 1), (4,2), (4, 6), (5, 2), (6, 4)]

adList = [[] for vertext in vertextList]

for edge in edgeList:
    adList[edge[0]].append(edge[1])

print(adList)



def dfs(adList):
    stack = [0]
    visitedVertex = []
    while stack:
        current = stack.pop()
        for neighbor in adList[current]:
            if not neighbor in visitedVertex:
                stack.append(neighbor)
        visitedVertex.append(current)
    return visitedVertex

print(dfs(adList))