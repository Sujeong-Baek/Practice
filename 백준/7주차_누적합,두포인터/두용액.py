# https://www.acmicpc.net/problem/2470
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    left = 0
    right = n-1
    answer = []
    zero = float('inf')
    while left < right:
        mix = nums[left] + nums[right]

        if zero > abs(mix):
            zero = abs(mix)
            answer = [nums[left], nums[right]]

        if mix < 0:
            left += 1
        
        elif mix > 0:
            right -= 1
        
        else:
            break


    for a in answer:
        print(a, end=' ')
solution()