# https://www.acmicpc.net/problem/1932
def solution():
    N = int(input())
    level = [list(map(int, input().split())) for _ in range(N)]
    answer = [[0]*i for i in range(1, N+1)]
    answer[0][0] = level[0][0]

    for i in range(N-1):
        for j in range(len(level[i])):
            answer[i+1][j] = max(answer[i+1][j], level[i+1][j] + answer[i][j])
            answer[i+1][j+1] = max(answer[i+1][j+1], level[i+1][j+1] + answer[i][j])
        
    print(max(answer[-1]))
    
solution()