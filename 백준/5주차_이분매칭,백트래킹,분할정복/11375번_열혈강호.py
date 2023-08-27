# https://www.acmicpc.net/problem/11375
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
adj = defaultdict(list)
for employee in range(1, N+1):
    tasks = list(map(int, sys.stdin.readline().split()))[1:]
    adj[employee].extend(tasks)

def dfs(employee):
    if visited[employee]:
        return False
    visited[employee] = True
    for task in adj[employee]:
        if match_task[task] == 0:
            match_task[task] = employee
            return True
        if not visited[match_task[task]] and dfs(match_task[task]):
            match_task[task] = employee
            return True
    return False

count = 0 
match_task = [0] * (M+1)
for employee in range(1, N+1):
    visited = [False] * (N+1)
    if dfs(employee):
        count += 1 
        if count == N:
            break
print(count)