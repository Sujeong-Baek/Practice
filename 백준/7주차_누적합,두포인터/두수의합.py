# https://www.acmicpc.net/problem/3273
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    nums = list(map(int, input().split()))
    x = int(input())
    

    nums.sort()

    left = 0 
    right = n - 1
    answer = 0
    print(nums)
    while left < right:
        total = nums[left] + nums[right]

        if total == x:
            answer += 1
            left += 1

        elif total > x:
            right -= 1

        else:
            left += 1
    print(answer)

solution()