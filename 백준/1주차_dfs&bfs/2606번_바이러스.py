# https://www.acmicpc.net/problem/2606
from collections import defaultdict, deque
def solution():
    computer = int(input())
    N = int(input())
    graph = defaultdict(list)

    for _ in range(N):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    visited = [0] * (computer+1)
    que = deque()
    que.append(1)
    visited[1] = 1
    count = 0
    while que:
        n = que.popleft()

        for neighbor in graph[n]:
            if visited[neighbor] == 0:
                count += 1
                que.append(neighbor)
                visited[neighbor] = 1
    print(count)
    
solution()