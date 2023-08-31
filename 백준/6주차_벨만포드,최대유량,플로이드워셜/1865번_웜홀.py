# https://www.acmicpc.net/problem/1865
import sys
input = sys.stdin.readline
t = int(input())

def bellman_ford(start, N, edges):
    costs = [sys.maxsize] * (N+1)
    costs[start] = 0
    
    for _ in range(N-1):
        for s, e, t in edges:
            if costs[e] > costs[s]+t:
                costs[e] = costs[s]+t

    for s, e, t in edges:
        if costs[e] > costs[s]+t:
            return True
    return False


for _ in range(t):
    N, M, W = map(int, input().split())
    edges = []
 
    for _ in range(M):
        s, e, t = map(int, input().split())
        edges.append((s,e,t))
        edges.append((e,s,t))
        
    for _ in range(W):
        s, e, t = map(int, input().split())
        edges.append((s,e,-t))

    
    for i in range(1, N+1):
        if bellman_ford(i, N, edges):
            print('YES')
            break
    else:
        print('NO')
