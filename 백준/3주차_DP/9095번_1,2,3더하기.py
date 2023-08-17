# https://www.acmicpc.net/problem/9095
def solution():
    N = int(input())
    nums = list(int(input()) for _ in range(N))

    count = [0] * (max(nums)+1)
    count[1] = 1
    count[2] = 2
    count[3] = 4

    answer = []

    for num in nums:
        if num < 4:
            answer.append(count[num])
        else:
            for i in range(4, num+1):
                count[i] = count[i-1] + count [i-2] + count[i-3]
            answer.append(count[i])

    print(answer)

solution()