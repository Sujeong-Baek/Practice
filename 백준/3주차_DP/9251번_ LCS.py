# https://www.acmicpc.net/problem/9251
def solution():
    A = list(map(str, input()))
    B = list(map(str, input()))
    lenA = len(A)
    lenB = len(B)

    dp = [[0] * (lenB + 1) for _ in range(lenA+1)]

    for i in range(1, lenA + 1):
        for j in range(1, lenB + 1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp)
    print(dp[lenA][lenB])

solution()