# https://www.acmicpc.net/problem/10448
def solution():
    T = int(input())
    for _ in range(T):
        N = int(input())
        num = 0
        count = 0
        while num<N:
            count += 1
            num += count
            print(num)
            if num == N:
                print(1)
                break

        if num > N:
            print(0)
solution()