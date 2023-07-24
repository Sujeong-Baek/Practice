# https://www.acmicpc.net/problem/2178
import sys
from collections import deque
def main():
    R, C =  map(int, sys.stdin.readline().split())
    MAP = [list(map(int, str(input()))) for _ in range(R)]

    visited = [[0]*C for _ in range(R)]
    count = 1
    que = deque()
    que.append((0,0,count))
    visited[0][0] = 1

    while que:
        r, c, count = que.popleft()
        if r == R-1 and c == C-1:
            print(count)
            return

        for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < R and 0 <= nc < C and MAP[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                que.append((nr, nc, count+1))


main()