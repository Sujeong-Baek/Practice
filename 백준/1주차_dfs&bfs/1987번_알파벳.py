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



def solution2():
    R, C = map(int, input().split())
    MAP = [list(map(lambda x : ord(x)-65, input())) for _ in range(R)]
    alphabet = [0]*26
    visited = [[0]*C for _ in range(R)]
    count = 0
    print(dfs(MAP, R, C, 0, 0, alphabet, count, visited))

    return

def dfs(MAP, R, C, r, c, alphabet, count, visited):
    count+=1
    count_list = [count]
    visited[r][c]=1
    alphabet[MAP[r][c]] = 1

    for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
        nr = dr + r
        nc = dc + c

        if 0 <= nr < R and 0 <= nc < C and alphabet[MAP[nr][nc]] == 0 and visited[nr][nc] == 0:
            count_list.append(dfs(MAP, R, C, nr, nc, alphabet, count, visited))
    visited[r][c]=0
    alphabet[MAP[r][c]] = 0 

    return max(count_list)

solution2()
