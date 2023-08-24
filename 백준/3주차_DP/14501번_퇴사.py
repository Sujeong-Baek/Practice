# https://www.acmicpc.net/problem/14501
def soluion():
    N = int(input())
    schedule = [list(map(int, input().split())) for _ in range(N)]
    dp = [0] * (N+1)
    for i, (t, p) in enumerate(schedule):
        if i+t <= N:
            dp[i+t] = max(max(dp[:i+1]) + p, dp[i+t])
        dp[i+1] = max(dp[:i+2])
    
    print(dp[-1])
soluion()