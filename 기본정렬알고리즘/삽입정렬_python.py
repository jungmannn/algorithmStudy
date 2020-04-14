alist = [3, 4, 9, 8, 7, 5, 2, 6, 1]

# def insertion_sort_Me(anyList):
#     k = 0
#     for i in range(0, len(anyList)):
#         max_idx = i
#         for k in range(i + 1, len(anyList) - i):
#             if anyList[max_idx] < anyList[k]:
#                 max_idx = k
#         temp = anyList[max_idx]
#         anyList[max_idx] = anyList[-i]
#         anyList[-i] = anyList[max_idx]

#     return anyList

# print(insertion_sort_Me(alist))


def insertion_sort(anyList):
    for i in range(1, len(anyList)):
        for j in range(i, 0, -1):
            if anyList[j] < anyList[j-1]:
                anyList[j], anyList[j-1] = anyList[j-1], anyList[j]
            else: break
    return anyList

print(insertion_sort(alist))