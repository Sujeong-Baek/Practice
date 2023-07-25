# https://www.acmicpc.net/problem/2667
from collections import deque
def solution():
    N =  int(input())
    MAP = [list(map(int, str(input()))) for _ in range(N)]
    total = 0
    house = []
    for r in range(N):
        for c in range(N):
            if MAP[r][c] == 1:
                total += 1
                house.append(bfs(MAP, N, r, c))

    print(total)
    for h in sorted(house):
        print(h)

    return
 
def bfs(MAP, N, R, C):

    que = deque()
    count = 1
    que.append((R, C))
    MAP[R][C] = 0

    while que:
        r, c = que.popleft()

        for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N and MAP[nr][nc] == 1:
                MAP[nr][nc] = 0
                count += 1
                que.append((nr, nc))


    return count

solution()