# acmicpc.net/problem/2644
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
    que.append((Node1, 0))
    visited = [0] * (Total+1)
    visited[Node1] = 1
    

    while que:
        n, count = que.popleft()
        if n == Node2:
            print(count)
            return

        for neighber in graph[n]:
            if visited[neighber] == 0:
                visited[neighber] = 1
                que.append((neighber, count+1))
    print(-1)

solution()