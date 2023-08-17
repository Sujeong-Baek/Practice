# https://www.acmicpc.net/problem/1463
def solution():
    N = int(input())
    count =[float('inf')] * (N+1)
    count[1] = 0
    for num in range(1, N+1):
        if num+1 <= N:
            count[num+1] = min(count[num+1], count[num]+1)
        if num*2 <= N:
            count[num*2] = min(count[num*2], count[num]+1) 
        if num*3 <= N: 
            count[num*3] = min(count[num*3], count[num]+1)
    print(count[-1])

solution()