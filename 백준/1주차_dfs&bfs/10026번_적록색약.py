# https://www.acmicpc.net/problem/10026
from collections import deque
def solution():
    N =  int(input())
    false_MAP = [list(map(str, input())) for _ in range(N)]
    true_MAP = [['R' if cell == 'G' else cell for cell in row] for row in false_MAP]

    f_total = 0
    t_total = 0

    for r in range(N):
        for c in range(N):
            if false_MAP[r][c] != 0:
                f_total += 1
                f_color = false_MAP[r][c]
                bfs(N, false_MAP, r, c, f_color)
            if true_MAP[r][c] != 0:
                t_total += 1
                t_color = true_MAP[r][c]
                bfs(N, true_MAP, r, c, t_color)
                
    print(f_total,t_total)
    return

def bfs(N, MAP, R, C, color):
    MAP[R][C] = 0
    que = deque()
    que.append((R, C))

    while que:
        r, c = que.popleft()

        for dr, dc in [[0,-1], [0,1], [1,0], [-1,0]]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N and MAP[nr][nc] == color:
                MAP[nr][nc] = 0     
                que.append((nr, nc))

solution()