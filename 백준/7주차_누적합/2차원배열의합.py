# https://www.acmicpc.net/problem/2167
import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    premix_sum = [[0]*(m+1) for _ in range(n+1)]

    for r in range(1, n+1):
        for c in range(1, m+1):
            premix_sum[r][c] = premix_sum[r-1][c] + premix_sum[r][c-1] - premix_sum[r-1][c-1] + board[r-1][c-1]

    t = int(input())
    for _ in range(t):
        i1, j1, i2, j2 = map(int, input().split())
        print(premix_sum[i2][j2] - premix_sum[i1-1][j2] - premix_sum[i2][j1-1] + premix_sum[i1-1][j1-1])

solution()