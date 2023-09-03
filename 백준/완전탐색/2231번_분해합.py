# https://www.acmicpc.net/problem/2231
def solution():
    N = int(input())
    num = 1
    answer = 0
    while num < N:
        s = str(num)
        total = num
        for i in range(len(s)):
            total += int(s[i])
        if total == N:
            answer = num
            break
        num += 1

    print(answer)

solution()