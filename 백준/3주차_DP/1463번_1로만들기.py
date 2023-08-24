# https://www.acmicpc.net/problem/1463
def solution():
    N = int(input())
    count =[float('inf')] * (N+1)
    count[N] = 0
    for i in range(N, 0, -1):
        if i%3 == 0:
            count[i//3] = min(count[i//3], count[i] + 1)
        if i%2 == 0:
            count[i//2] = min(count[i//2], count[i] + 1)
        if i - 1 > 0:
            count[i-1] = min(count[i-1], count[i]+1)

    print(count[1])
            
solution()