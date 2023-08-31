# https://www.acmicpc.net/problem/11657
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

def bellman_ford(N, edges):
    costs = [sys.maxsize] * (N+1)
    costs[1] = 0

    for _ in range(N+1):
        for s, e, t in edges:
            if costs[s] != sys.maxsize and costs[e] > costs[s]+t:
                costs[e] = costs[s]+t
    
    for s, e, t in edges:
        if costs[s] != sys.maxsize and costs[e] > costs[s]+t:
            return [-1]
        
    return costs



edges = []
for _ in range(M):
    s, e, t = map(int, input().split())
    edges.append((s,e,t))

answer = bellman_ford(N, edges)

if answer[0] == -1:
    print(-1)
else:
    for a in answer[2:]:
        if a == sys.maxsize:
            print(-1)
        else:
            print(a)

