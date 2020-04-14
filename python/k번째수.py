import sys

array = list(map(int, sys.stdin.readline().split()))
commands = list()
for n in range(0, 3):
    command = list(map(int, sys.stdin.readline().split()))
    commands.append(command)

def solution(array, commands):
    answer = list()
    for n in range(len(commands)):
        i = commands[n][0]
        j = commands[n][1]
        k = commands[n][2]
        
        array_command = array[i-1 : j]
        array_command.sort()
        key = array_command[k - 1]
        answer.append(key)
    return answer

print(solution(array, commands))
