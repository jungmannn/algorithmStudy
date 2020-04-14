from operator import eq
import sys

participant = list( sys.stdin.readline().split())
completion = list(sys.stdin.readline().split())



def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    flag = True

    for i in range(len(completion)):
        if not eq(participant[i], completion[i]):
            answer = participant[i]
            flag = False
            break
    if flag:
        answer = participant[-1]
    return answer


result = solution(participant, completion)

print(result)
