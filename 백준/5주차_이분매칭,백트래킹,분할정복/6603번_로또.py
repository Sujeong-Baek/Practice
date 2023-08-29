# https://www.acmicpc.net/problem/6603
from itertools import combinations
def solution():
    
    while  True:
        nums = list(map(int, input().split()))
        if nums[0] == 0:
            break
        
        for combi in combinations(nums[1:], 6):
            print(' '.join(map(str, list(combi))))


from sys import stdin

def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end=' ')
        print()
        return

    for i in range(start, len(s)):
        combi[depth] = s[i]
        dfs(i+1, depth+1)

while True:
    data = list(map(int, stdin.readline().split()))
    if data[0] == 0:
        break

    s = data[1:]
    combi = [0] * 13
    dfs(0, 0)
    print()