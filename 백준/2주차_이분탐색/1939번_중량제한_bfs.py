# https://www.acmicpc.net/problem/1939
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    left = 1
    right = 0
    answer = 0
    graph = defaultdict(list)

    for _ in range(M):
        n1, n2, w = map(int, input().split())
        right = max(right, w)
        graph[n1].append((n2, w))
        graph[n2].append((n1, w))

    S, E = map(int, input().split())

    while left <= right:
        mid = (left+right)//2

        que = deque([S])
        visited = [False] * (N+1)
        visited[S] = True
        flag = False
        while que:
            current = que.popleft()
            for neighber, w in graph[current]:
                if mid<= w and visited[neighber] == False:
                    if neighber == E:
                        flag = True
                        break
                    visited[neighber] = True
                    que.append(neighber)
            if flag:
                break

        if flag == False:
            right = mid-1

        else:
            left = mid + 1
            answer = max(answer, mid)

    print(answer)


solution()



