# https://www.acmicpc.net/problem/3079
import sys
def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    times = [int(input()) for _ in range(N)]
    left = 0
    right = min(times)*M
    while left< right:
        mid = (left + right)//2
        total = sum([mid//time for time in times])
        if total < M:
            left = mid + 1
        else:
            right = mid -1
    print(right)
solution()