# https://www.acmicpc.net/problem/11403
def solution():
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]


    for k in range(N):
        for i in range(N):
            if graph[i][k]:
                for j in range(N):
                    if graph[k][j]:
                        graph[i][j] = 1
    for row in graph:
        print(*row)

solution()