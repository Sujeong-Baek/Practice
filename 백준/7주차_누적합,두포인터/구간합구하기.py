# https://www.acmicpc.net/problem/11659
def solution():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    sections = [list(map(int, input().split())) for _ in range(M)]
    prefix_sum = [0] * (N+1)

    for idx, num in enumerate(nums):
        prefix_sum[idx+1] = prefix_sum[idx] + num
    
    for i, j in sections:
        print(prefix_sum[j]-prefix_sum[i-1])
solution()