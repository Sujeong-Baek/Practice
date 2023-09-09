# https://www.acmicpc.net/problem/1298
from collections import deque

def solution():
    def bfs(dist):
        queue = deque()
        for i in range(1, n+1):
            if not matched_A[i]:
                dist[i] = 0
                queue.append(i)
            else:
                dist[i] = float('inf')
        dist[0] = float('inf')
        while queue:
            a = queue.popleft()
            if a:
                for b in adj[a]:
                    if dist[matched_B[b]] == float('inf'):
                        dist[matched_B[b]] = dist[a] + 1
                        queue.append(matched_B[b])
        return dist[0] != float('inf')

    def dfs(a, dist):
        if a:
            for b in adj[a]:
                if dist[matched_B[b]] == dist[a] + 1 and dfs(matched_B[b], dist):
                    matched_A[a] = b
                    matched_B[b] = a
                    return True
            dist[a] = float('inf')
            return False
        return True

    n, m = map(int, input().split())
    if m == 0:
        print(0)
        return
        
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        student, notebook = map(int, input().split())
        adj[student].append(notebook)

    matched_A = [0 for _ in range(n+1)]
    matched_B = [0 for _ in range(n+1)]
    dist = [0 for _ in range(n+1)]
    match_count = 0

    while bfs(dist):  # pass dist as an argument
        for i in range(1, n+1):
            if not matched_A[i] and dfs(i, dist):  # pass dist as an argument
                match_count += 1

    print(match_count)
