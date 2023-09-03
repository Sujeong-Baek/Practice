# https://www.acmicpc.net/problem/2798
from itertools import combinations
def solution():
    n, m = map(int, input().split())
    cards = set(map(int, input().split()))
    answer = 0
    for select in combinations(cards, 3):
        total = sum(select)
        if total <= m:
            answer = max(answer, total)
    
    print(answer)

solution()