target = 3
number = [1, 1, 1, 1, 1]

def solution(number, target):
    answer_tree = [0]
    
    for num in number:
        node_list = []
        for an in answer_tree:
            node_list.append(an + num)
            node_list.append(an - num)
        answer_tree = node_list
    answer = answer_tree.count(target)
    return answer

print(solution(number, target))