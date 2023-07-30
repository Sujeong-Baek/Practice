# https://www.acmicpc.net/problem/5014
from collections import deque
def solution():
    Total, Start, End, Up , Down = map(int, input().split())
    que = deque()
    que.append((Start, 0))
    visited = [0] *(Total+1)
    visited[Start] = 1

    while que:
        floor, count = que.popleft()
        if floor == End:
            print(count)
            return
        
        for move in [floor+Up, floor-Down]:
            if 0 < move <= Total and visited[move] == 0:
                que.append((move, count+1))
                visited[move] = 1
    print('use the stairs')

solution()