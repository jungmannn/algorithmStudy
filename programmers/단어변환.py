
begin = "hit"

target = "cog"

words = ["hot", "dot", "dog", "lot", "log", "cog"]

def solution(begin, target, words):
    lenTrans = 0

    for w in words:
        if w == begin:
            break
        lenTrans += 1
    
    if target not in words:
        return 0
    
    return lenTrans


print(solution(begin, target, words))