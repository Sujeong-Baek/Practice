# https://www.acmicpc.net/problem/2178
import sys
from collections import deque
def main():
    R, C =  map(int, sys.stdin.readline().split())
    MAP = [list(map(int, str(input()))) for _ in range(R)]

    visited = [[0]*C for _ in range(R)]
    que = deque()
    que.append((0,0))
    visited[0][0] = 1

    while que:
        r, c = que.popleft()
        if r == R-1 and c == C-1:
            print(visited[R-1][C-1])
            return

        for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < R and 0 <= nc < C and MAP[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                que.append((nr, nc))

main()