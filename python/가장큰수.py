import sys
from itertools import permutations

numbers = [6, 10, 2]

numbers = list(map(str, numbers))
numbers.sort(key = lambda x : x*3, reverse=True)

print(numbers)

# print(str(int(''.join(numbers))))
