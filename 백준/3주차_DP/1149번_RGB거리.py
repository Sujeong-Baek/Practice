# https://www.acmicpc.net/problem/1149
def solution():
    N = int(input())
    RGB = [list((map(int, input().split()))) for _ in range(N)]
    memo = [[0]*3 for _ in range(N)]
    memo[0] = RGB[0]
    
    for i in range(1,N):
        for j in range(3):
            memo[i][j] = min(memo[i-1][(j+1)%3], memo[i-1][(j+2)%3]) + RGB[i][j]
    print(min(memo[-1]))        

solution()


def solution2():
    N = int(input())
    RGB_costs = [list((map(int, input().split()))) for _ in range(N)]
    dp = [RGB_costs[0]]
    
    for i in range(1,N):
        current_cost = [
            RGB_costs[i][j] + min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3]) for j in range(3)
        ]
        dp.append(current_cost)
    print(min(dp[-1]))        

solution2()