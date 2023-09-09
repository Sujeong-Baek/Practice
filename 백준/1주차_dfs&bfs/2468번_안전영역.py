# https://www.acmicpc.net/problem/2468
from collections import deque
def solution():
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    max_high = max(max(row) for row in MAP)
    answer = 0

    for h in range(max_high+1):
        temp_MAP = [row[:] for row in MAP]
        count = 0
        for r in range(N):
            for c in range(N):
                if temp_MAP[r][c]>h:
                    count += 1
                    bfs(temp_MAP, N, r, c, h)
        answer = max(answer, count)
    print(answer)                    
    
def bfs(Map, N, R, C, h):
    que= deque()
    que.append((R,C))
    Map[R][C] = 0
    
    while que:
        r, c = que.popleft()

        for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
            nr = r+dr
            nc = c+dc
            if 0<= nr < N and 0 <= nc < N and Map[nr][nc] > h:
                Map[nr][nc] = 0
                que.append((nr, nc))

solution()