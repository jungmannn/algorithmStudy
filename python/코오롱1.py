import sys

price = int(input())
info = []
for i in range(0, 4):
    info.append(list(map(int, input().split())))

def soultion(price, info):
    result = []
    dict_info = dict()
    # sorted_info = sorted(info, key=lambda x: x[0])
    for n in range(len(info)):
        dict_info[n+1] = info[n] 
    list_info = dict_info.items()
    print(list_info)
    for i in list_info:
        result.append((i[0], [i[1][0], price * i[1][0] + i[1][1]]))
    print(result)
    sorted_result = sorted(result, key=lambda x: (x[1][1], x[1][0]))
    print(sorted_result)
    
    answer = sorted_result[0][0]
    return answer

print(soultion(price, info))