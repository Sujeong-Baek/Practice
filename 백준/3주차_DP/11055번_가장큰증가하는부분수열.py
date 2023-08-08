# https://www.acmicpc.net/problem/11055
def solution():
    N = int(input())
    A = list(map(int, input().split()))
    count = A.copy()

    for i in range(1, N):
        for j in range(i):
            if A[i] > A[j]:
                count[i] = max(count[j]+A[i], count[i])
    print(max(count))
solution()

