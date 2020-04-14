
# # first way
n = 10

lost = [1, 5, 8, 3, 7]
reserve = [7, 5, 2, 9, 6]

# u = [1] * (n + 2)

# for i in reserve:
#     u[i] += 1
# for i in lost:
#     u[i] -= 1
# print(u)
# for i in range(1, n + 1):
#     if u[i - 1] == 0 and u[i] == 2:
#         u[i - 1:i + 1] = [1, 1]
#     elif u[i] == 2 and u[i + 1] == 0:
#         u[i : i + 2] = [1, 1]

# print(u)

# print(len([x for x in u[1:-1] if x>0]))

# second way

# s = set(lost) & set(reserve)
# l = set(lost) - s

realLost = [i for i in lost if i not in reserve]
realReserve = [i for i in reserve if i not in lost]
print(realLost)
print(realReserve)

for i in sorted(realReserve):
    if i - 1 in realLost:
        realLost.remove(i-1)
    elif i + 1 in realLost:
        realLost.remove(i + 1)
print(n - len(realReserve))