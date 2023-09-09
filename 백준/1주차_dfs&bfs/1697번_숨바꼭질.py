# https://www.acmicpc.net/problem /1697
from collections import deque
def solution():
    S, E = map(int, input().split())
    que = deque()
    que.append(S)
    visited = [-1] * 100001
    visited[S] = 0
    
    while que:
        point = que.popleft()
        if point == E:
            print(visited[point])
            return

        for move_point in [point+1, point-1, point*2]:
            if 0<= move_point < len(visited) and visited[move_point] == -1:
                que.append(move_point)
                visited[move_point] = visited[point] + 1
solution()