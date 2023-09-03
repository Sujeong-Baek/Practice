# https://www.acmicpc.net/problem/1436
def solution():
    N = int(input())

    n = 1
    num = 666

    while n<N:
        num += 1
        if '666' in str(num):
            n+=1

    print(num)
solution()