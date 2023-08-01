# https://www.acmicpc.net/problem/1939
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = defaultdict(list)
    left = 0
    right = 0
    answer = 0

    for _ in range(M):
        n1, n2, w = map(int, input().split())
        right = max(right, w)
        graph[n1].append((n2, w))
        graph[n2].append((n1, w))

    S, E = map(int, input().split())
    
    while left<=right:
        mid = (left+right)//2
        visited = [False]*(N+1)
        dfs(graph, S, mid, visited)

        if visited[E] == False:
            right = mid -1
        else:
            answer = max(answer, mid)
            left = mid + 1
    print(answer)


def dfs(graph, node, mid, visited):
    visited[node] = True
    prev = None
    for neighber, weight in sorted(graph[node], key = lambda x: (x[0], -x[1])):
        if prev != neighber and weight >= mid and visited[neighber]is False:
            dfs(graph, neighber, mid, visited)
            prev = neighber

solution()
