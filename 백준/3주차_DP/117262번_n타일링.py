# https://www.acmicpc.net/problem/11726
def solution():
    N = int(input())
    if N == 1:
        print(1)
        return
    if N == 2:
        print(2)
        return
    
    dp = [0] * (N+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N+1):
        dp[i] = dp[i-2]+dp[i-1]
    
    print(dp[-1]%10007)

solution()