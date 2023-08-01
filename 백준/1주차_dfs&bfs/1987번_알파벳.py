# https://www.acmicpc.net/problem/1987
from collections import deque
def solution():
    R, C = map(int, input().split())
    MAP = [list(map(lambda x : ord(x)-65, input())) for _ in range(R)]

    alphabet = [0]*26
    que = deque()
    que.append((0, 0, alphabet))
    alphabet[MAP[0][0]] = 1

    max_count = [[0] * C for _ in range(R)]
    max_count[0][0] = 1

    while que:
        r, c, alphabet = que.popleft()
        for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
            nr = dr + r
            nc = dc + c

            if 0 <= nr < R and 0 <= nc < C and alphabet[MAP[nr][nc]] == 0:
                current_count = max_count[r][c] + 1
                current_alphabet = [a for a in alphabet]
                current_alphabet[MAP[nr][nc]] = 1
                que.append((nr, nc, current_alphabet))
                
                if max_count[nr][nc] < current_count:
                    max_count[nr][nc] = current_count

    print(max([max(r) for r in max_count]))
    return

solution()




import sys
input=sys.stdin.readline
def dfs(r, c, count):
    global mx
    mx = max(mx,count)
    for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
        nr = dr + r
        nc = dc + c
        if (0<=nr<R) and (0<=nc<C) and (alpha_check[int(ord(graph[nr][nc]))-65]==False):
            alpha_check[int(ord(graph[nr][nc]))-65]=True
            dfs(nr, nc, count+1)
            alpha_check[int(ord(graph[nr][nc]))-65]=False
R, C=map(int, input().split())
graph=[]
for _ in range(R):
    graph.append(list(input().strip()))
alpha_check=[False]*26
mx=1
alpha_check[int(ord(graph[0][0]))-65]=True
dfs(0, 0, 1)
print(mx)




dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def dfs(r, c, path):
    global result
    result = max(result, len(path))

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in path:
            dfs(nr, nc, path + board[nr][nc])

R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input().strip()))
result = 0
dfs(0, 0, board[0][0])
print(result)