# https://www.acmicpc.net/problem/11441
import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    premix_sum = [0]
    for i in range(N):
        premix_sum.append(premix_sum[i]+nums[i])
        
    T = int(input())
    for _ in range(T):
        i, j = map(int, input().split())
        print(premix_sum[j] - premix_sum[i-1])

solution()