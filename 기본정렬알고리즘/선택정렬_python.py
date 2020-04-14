
alist = [3, 4, 9, 8, 7, 5, 2, 6, 1]
# alist.sort()

def selection_sort(anyList):
    for i in range(0, len(anyList) - 1):
        min_idx = i
        for k in range(i + 1, len(anyList)):
            if anyList[min_idx] > anyList[k]:
                min_idx = k
        temp = anyList[i]
        anyList[i] = anyList[min_idx]
        anyList[min_idx] = temp
    return anyList


print(selection_sort(alist))