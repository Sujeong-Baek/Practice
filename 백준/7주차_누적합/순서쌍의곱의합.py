# https://www.acmicpc.net/problem/13900
import sys
input = sys.stdin.readline 
def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    premix_sum = [0]
    for i in range(N):
        premix_sum.append(premix_sum[i]+nums[i])
    
    answer = 0
    for i in range(1, N):
        answer += (premix_sum[N] - premix_sum[i]) * nums[i-1] 
    print(answer)

solution()