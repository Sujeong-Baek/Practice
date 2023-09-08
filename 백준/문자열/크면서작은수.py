# https://www.acmicpc.net/problem/2992
from itertools import permutations
def solution():
    N = list(map(int, input().strip()))
    answer = int(''.join(map(str, N)))
    
    for combi in permutations(N, len(N)):
        num = int(''.join(map(str, combi))) 
        if num > answer:
            answer = num
            print(answer)
            break
    else:
        print(0)
solution()