# https://www.acmicpc.net/problem/1520
import sys
sys.setrecursionlimit(10**6)
def solution():
    R, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]
    dp = [[-1]*C for _ in range(R)]
    print(dfs(board, R, C, 0, 0, dp))
    
def dfs(board, R, C, r, c, dp):
    if r == R-1 and c == C-1:
        return 1
    
    if dp[r][c] != -1:
        return dp[r][c]
    
    dp[r][c] = 0
    for dr, dc in [[1,0],[-1,0], [0,1], [0,-1]]:
        nr, nc = dr + r, dc + c
        if 0 <= nr < R and 0 <= nc < C and board[r][c] > board[nr][nc]:
            dp[r][c] += dfs(board, R, C, nr, nc,dp)
    return dp[r][c]

solution()