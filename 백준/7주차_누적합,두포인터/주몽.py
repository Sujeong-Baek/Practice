# https://www.acmicpc.net/problem/1940
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    m = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    left = 0
    right = n - 1
    answer = 0
    while left < right:
        total = nums[left] + nums[right]

        if total == m:
            answer += 1
            left += 1
        
        elif total < m:
            left += 1
        
        else:
            right -= 1

    print(answer)

solution()