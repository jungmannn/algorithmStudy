import sys

list1 = []

answer = [1,2,3,4,5]

aList = [1, 2, 3, 4, 5]
count = 0
for i in range(0, 5):
        if count < 5:
            list1.append(aList[count])
            count +=1
        else:
            count = 0

list2 = []

bList = [2, 1, 2, 3, 2, 4, 2, 5]
count = 0
for i in range(0, 5):
        if count < 8:
            list2.append(bList[count])
            count +=1
        else:
            count = 0

list3 = []

cList = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
count = 0
for i in range(0, 5):
        if count < 10:
            list3.append(cList[count])
            count +=1
        else:
            count = 0

answer_a = set(answer) - set(list1)
answer_b = set(answer) - set(list2)
answer_c = set(answer) - set(list3)

result = list()

# result.append(len(answer_a))
# result.append(len(answer_b))
# result.append(len(answer_c))

s = set(list2)
result = [x for x in answer if x not in s]

print(result)