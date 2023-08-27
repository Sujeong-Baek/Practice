# https://www.acmicpc.net/problem/15649
def backtrack(n, m, current):
    if len(current) == m:
        print(' '.join(map(str, current)))
        return
    
    for num in range(1,n+1):
        if num not in current:
            backtrack(n, m, current+[num])


def solution():
    n, m = map(int, input().split())
    backtrack(n, m, [])


solution()