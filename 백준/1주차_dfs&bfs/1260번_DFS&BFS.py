# https://www.acmicpc.net/problem/1260
from collections import defaultdict, deque
import sys

def bfs(graph, n, v):
    visited = [0] * (n+1)
    que = deque(([v]))
    visited[v]=1
    answer = []
    
    while que:
        node = que.popleft()
        answer.append(node)
        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                que.append(neighbor)
                visited[neighbor]=1
    return answer 


def dfs(graph, n, v, visited, answer):

    visited[v] = 1
    answer.append(v)

    for node in graph[v]:
        if visited[node] == 0:
            dfs(graph, n, node, visited, answer)
    return answer


def main():
    n, m, v = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)

    for _ in range(m):
        n1, n2 =  map(int, sys.stdin.readline().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    for node in graph:
        graph[node].sort()

    d_visited = [0] * (n+1)
    d_answer = []
    d = dfs(graph, n, v, d_visited, d_answer)
    b = bfs(graph, n, v)

    for node in d:
        print(node, end=' ')
    print()
    for node in b:
        print(node, end=' ')
    print()

main()
