# https://www.acmicpc.net/problem/1158
def solution():
    N, K = map(int, input().split())
    nums = [k+1 for k in range(N)]
    idx = K-1
    answer = []
    while len(nums)>0:
        answer.append(nums[idx])
        del nums[idx]
        idx += K-1

        if nums and idx >= len(nums):
            idx %= len(nums)

    print('<', end='')
    for i, a in enumerate(answer):
        if i != len(answer) -1:
            print(a, end=', ')
        else:
            print(f'{a}>')

solution()