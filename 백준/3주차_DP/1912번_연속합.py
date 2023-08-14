# https://www.acmicpc.net/problem/1912
def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    dp = nums.copy()
    
    for i in range(1, N):
        dp[i] = max(dp[i], dp[i-1]+nums[i])

    print(max(dp))

solution()