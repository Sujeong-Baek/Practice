# https://www.acmicpc.net/problem/2992
from itertools import permutations
def solution():
    N = list(map(int, input().strip()))
    target = int(''.join(map(str, N)))
    answer = float('inf')

    for combi in permutations(N, len(N)):
        num = int(''.join(map(str, combi))) 
        
        if num > target:
            answer = min(answer, num)

    if answer == float('inf'):
        print(0)
    else:
        print(answer)
solution()