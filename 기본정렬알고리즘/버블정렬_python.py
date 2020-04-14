alist = [4, 5, 2, 9, 7, 3, 6, 1, 8]

# def bubble_sort(anyList):
#     for j in range(0, len(anyList)):
#         k = len(anyList) - 2
#         for i in range(len(anyList) - 1, 0, -1):
#             if anyList[i] < anyList[k]:
#                 temp = anyList[i]
#                 anyList[i] = anyList[k]
#                 anyList[k] = temp
#             k -= 1
        
#     return anyList

def bubble_sort(anyList):
    for k in range(len(alist)-1,0,-1):
        for i in range(k):
            if anyList[i]>anyList[i+1]:
                temp = anyList[i]
                anyList[i] = anyList[i+1]
                anyList[i+1] = temp
    return anyList

print(bubble_sort(alist))