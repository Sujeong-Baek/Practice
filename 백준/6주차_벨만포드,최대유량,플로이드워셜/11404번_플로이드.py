# https://www.acmicpc.net/problem/11404
import sys
def solution():
    n = int(input())
    m = int(input())

    graph = [[float('inf')]*n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0

    for _ in range(m):
        s, e, c = map(int, sys.stdin.readline().split())
        graph[s-1][e-1] = min(graph[s-1][e-1], c)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
                
    for i in range(n):
        for j in range(n):
            if graph[i][j] == float('inf'):
                print(0, end=' ')
            else:
                print(graph[i][j], end=' ')
        print()
solution()