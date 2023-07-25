# https://www.acmicpc.net/problem/2206
import sys
from collections import deque
def solution():
    R, C =  map(int, sys.stdin.readline().split())
    MAP = [list(map(int, str(input()))) for _ in range(R)]
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    que = deque()
    que.append((0, 0, False, 1))

    costs = [[[float('inf')]*2 for _ in range(C)] for _ in range(R)]
    costs[0][0] = [1,1]


    while que:
        r, c, wall, count = que.popleft()
       

        if r == R-1 and c == C-1:
            print(min(costs[r][c]))
            return

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < R and 0 <= nc < C:
                current_count = count + 1

                if wall is False and MAP[nr][nc] == 0 and costs[nr][nc][0] > current_count: 
                    costs[nr][nc][0] = current_count
                    que.append((nr, nc, wall, current_count))
                
                elif wall is True and MAP[nr][nc] == 0 and costs[nr][nc][1] > current_count: 
                    costs[nr][nc][1] = current_count
                    que.append((nr, nc, wall, current_count))

                elif wall is False and MAP[nr][nc] == 1 and costs[nr][nc][1] > current_count:
                    costs[nr][nc][1] = current_count
                    que.append((nr, nc, True, current_count))
    print(-1)
    return

solution()


