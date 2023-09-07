# https://www.acmicpc.net/problem/2230
import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    nums = list(int(input()) for _ in range(n))
    nums.sort()

    min_diff = float('inf')
    left = 0
    right = 1

    while left < n and right < n:
        diff = nums[right] - nums[left]
        if diff < m:
            right += 1

        else:
            min_diff = min(diff, min_diff)
            left += 1
        

    print(min_diff)
solution()