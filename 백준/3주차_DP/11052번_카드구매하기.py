# https://www.acmicpc.net/problem/11052
def solution():
    N = int(input())
    cards = list(map(int, input().split()))
    dp = [0] + cards[:]
    
    for i in range(1, N+1):
        for count in range(i, N+1):
            dp[count] = max(dp[count], dp[count-i] + dp[i])
    print(dp[-1])
        
solution()