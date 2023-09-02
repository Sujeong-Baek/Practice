# https://www.acmicpc.net/problem/4963
from collections import deque
import sys
sys.setrecursionlimit(10**6)

def solution():
    answer = []
    while True:
        C, R = map(int, input().split())
        if R == 0 and C  == 0:
            break
        MAP = [list(map(int,input().split())) for _ in range(R)]
        total = 0
        for r in range(R):
            for c in range(C):
                if MAP[r][c] == 1 :
                    total += 1
                    bfs(MAP, R, C, r, c)
        answer.append(total)

    for a in answer:
        print(a)
    return

def bfs(MAP, R, C, r, c):
    que = deque()
    que.append((r, c))
    MAP[r][c] = 0
    while que:
        rr, cc = que.popleft()
        for dr, dc in [[1,0], [-1,0], [0,1], [0,-1], [1,1], [1,-1], [-1,1], [-1,-1]]:
            nr = rr + dr
            nc = cc + dc

            if 0 <= nr < R and 0 <= nc < C and MAP[nr][nc] == 1:
                MAP[nr][nc] = 0
                que.append((nr, nc))
    return



    
def solution2():
    answer = []
    while True:
        C, R = map(int, input().split())
        if R == 0 and C  == 0:
            break
        MAP = [list(map(int,input().split())) for _ in range(R)]
        total = 0
        for r in range(R):
            for c in range(C):
                if MAP[r][c] == 1 :
                    total += 1
                    dfs(MAP, R, C, r, c)
        answer.append(total)
    for a in answer:
        print(a)
    return

def dfs(MAP, R, C, r, c):
    MAP[r][c] = 0
    for dr, dc in [[1,0], [-1,0], [0,1], [0,-1], [1,1], [1,-1], [-1,1], [-1,-1]]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < R and 0 <= nc < C and MAP[nr][nc] == 1:
                dfs(MAP, R, C, nr, nc)

solution2()