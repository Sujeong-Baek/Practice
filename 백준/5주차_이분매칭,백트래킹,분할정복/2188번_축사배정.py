# https://www.acmicpc.net/problem/2188
from collections import defaultdict
def solution():
    N, M = map(int, input().split())
    requests = [list(map(int, input().split())) for _ in range(N)]
    requests = sorted(requests, key = lambda x: x[0])

    adj = defaultdict(list)
    for cow, request in enumerate(requests, 1):
        for cage in request[1:]:
            adj[cow].append(cage)

    def dfs(cow):
        if visited[cow]:
            return False
        visited[cow] = True

        for cage in adj[cow]:
            if match_cage[cage] == 0 or dfs(match_cage[cage]):
                match_cage[cage] = cow
                return True
        return False
        
    count = 0
    match_cage = [0] * (M+1)
    for cow in range(N+1):
        visited = [False] * (N+1)
        if dfs(cow):
            count += 1

    print(count)

solution()