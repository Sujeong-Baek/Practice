# https://www.acmicpc.net/problem/2644
from collections import defaultdict, deque
def solution():
    Total = int(input())
    Node1, Node2 = map(int, input().split())
    N = int(input())
    graph = defaultdict(list)
    for _ in range(N):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    que = deque()
    que.append(Node1)
    visited = [-1] * (Total+1)
    visited[Node1] = 0
    
    while que:
        n = que.popleft()
        if n == Node2:
            print(visited[n])
            return

        for neighber in graph[n]:
            if visited[neighber] == -1:
                visited[neighber] = visited[n] + 1
                que.append(neighber)
    print(-1)

solution()


def solution2():
    Total = int(input())
    Node1, Node2 = map(int, input().split())
    N = int(input())
    graph = defaultdict(list)
    for _ in range(N):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    visited = [-1] * (Total+1)
    visited[Node1] = 0
    dfs(Node1, visited, graph)
    print(visited[Node2])


def dfs(node, visited, graph):
    for neighber in graph[node]:
        if visited[neighber] == -1:
            visited[neighber] = visited[node]+1
            dfs(neighber, visited, graph)

solution2()
