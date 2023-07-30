# https://www.acmicpc.net/problem/1697
from collections import deque
def solution():
    S, E = map(int, input().split())
    que = deque()
    que.append((S, 0))
    visited = [0] * 100001
    visited[S] = 0
    
    while que:
        point, count = que.popleft()
        if point == E:
            print(count)
            return

        for move_point in [point+1, point-1, point*2]:
            if 0<= move_point < len(visited) and visited[move_point] == 0:
                que.append((move_point, count+1))
                visited[move_point] = 1
solution()