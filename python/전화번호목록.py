
# phone_book = ["123", "456", "789"]

# def solution(phone_book):
#     answer = True
#     d = dict()
#     list1 =list()

#     for i in phone_book:
#         d[i] = d.get(i, 0) + len(i)
    
#     for i in phone_book:
#         for j in phone_book:
#             list1.append(j[0 : d[i]])
        
#         if len(set(list1)) != len(list1):
#             answer = False
#         list1 = []
#     return answer


# print(solution(phone_book))


phone_book = ["123","456","789"]

def solution(phone_book):
    answer = True
    
    d = dict()
    list1 = list()
    for i in range(0, len(phone_book) - 1):
        for j in range(i, len(phone_book) - 1):
            search = phone_book[i]
            list1.append(phone_book[j+1].find(search))
    
    if list1.count(0) != 0:
        answer = False

    return answer


print(solution(phone_book))