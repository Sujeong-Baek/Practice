# https://www.acmicpc.net/problem/1654
def solution():
    K, N = map(int, input().split())
    lines = [int(input()) for _ in range(K)]
    left = 1
    right = max(lines)
    while left < right:
        mid = (left+right)//2
        total = sum([line//mid for line in lines if line>=mid])
        if total < N:
            right = mid-1
        else:
            left = mid+1
    total = sum([line//left for line in lines if line>=left])
    if total < N:
        print(left-1)
    else:
        print(left)
solution()