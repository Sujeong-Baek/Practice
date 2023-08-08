# https://www.acmicpc.net/problem/11722
def solution():
    N = int(input())
    A = list(map(int, input().split()))
    count = [1] * N

    for i in range(1,N):
        for j in range(i):
            if A[i] < A[j]:
                count[i] = max(count[j]+1, count[i])

    print(max(count))
    
solution()