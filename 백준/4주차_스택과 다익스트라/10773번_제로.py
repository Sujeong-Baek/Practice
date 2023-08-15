# https://www.acmicpc.net/problem/10773
def solution():
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    total = []

    for num in nums:
        if total and num == 0:
            total.pop()
        elif num != 0:
            total.append(num)
    print(sum(total))

solution()