# https://www.acmicpc.net/problem/2156
def solution():
    N = int(input())
    wines = [int(input()) for _ in range(N)]
    dp = [0] * N
    if len(wines) == 1:
        print(wines[0])
        return
    if len(wines) == 2:
        print(sum(wines))
        return
    if len(wines) == 3:
        print(max(wines[0]+wines[2], wines[1]+wines[2], wines[0]+wines[1]))
        return
    
    dp[0] = wines[0]
    dp[1] = dp[0] + wines[1]
    dp[2] = max(wines[0]+wines[2], wines[1]+wines[2], dp[1])

    for i in range(3, N):
        dp[i] = max(dp[i-2]+wines[i], dp[i-3]+wines[i-1]+wines[i], dp[i-1])
    print(dp[-1])

solution()