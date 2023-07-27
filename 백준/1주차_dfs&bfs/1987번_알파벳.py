# https://www.acmicpc.net/problem/1987
from collections import deque
def solution():
    R, C = map(int, input().split())
    MAP = [list(map(str, input())) for _ in range(R)]
    alphabet = []
    visited = [[0]*C for _ in range(R)]
    count = 0
    print(dfs(MAP, R, C, 0, 0, alphabet, count, visited))

    return

def dfs(MAP, R, C, r, c, alphabet, count, visited):
    

    visited[r][c] = count+1
    print(r, c, visited)
    current_alphabet = set(a for a in alphabet)
    current_alphabet.add(MAP[r][c])
    
    for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
        nr = dr + r
        nc = dc + c

        if 0 <= nr < R and 0 <= nc < C and MAP[nr][nc] not in alphabet and visited[nr][nc]<visited[r][c]+1:
            print(nr, nc)
            dfs(MAP, R, C, nr, nc, current_alphabet, count+1, visited) 

    return max([max(r) for r in visited])
solution()