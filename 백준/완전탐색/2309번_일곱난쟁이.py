# https://www.acmicpc.net/problem/2309
from itertools import combinations
def solution():
    high = (int(input()) for _ in range(9))
    answer = []
    for seven in combinations(high, 7):
        total = sum(seven)
        if total == 100:
            answer = list(seven)
            break

    answer.sort()
    for a in answer:
        print(a)
    
solution()