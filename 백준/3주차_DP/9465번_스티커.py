# https://www.acmicpc.net/problem/9465
def solution():
    T = int(input())
    for _ in range(T):
        N = int(input())
        stickers = [list(map(int, input().split())) for _ in range(2)]
        print(serch_max_score(N, stickers))



def serch_max_score(N, stickers):
    if N == 1:
        return max(stickers[0][0], stickers[1][0])
    
    memo = [[0]*N for _ in range(2)]
    memo[0][0] = stickers[0][0]
    memo[0][1] = stickers[0][1] + stickers[1][0]
    memo[1][0] = stickers[1][0]
    memo[1][1] = stickers[1][1] + stickers[0][0]

    for i in range(2, N):
        memo[0][i] = max(memo[1][i-1], memo[1][i-2]) + stickers[0][i]
        memo[1][i] = max(memo[0][i-1], memo[0][i-2]) + stickers[1][i]
    return max(memo[0][N-1], memo[1][N-1])
        
            
solution()