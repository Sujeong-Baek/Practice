# https://www.acmicpc.net/problem/2839
def solution():
    sugar = int(input())
    num = [float('inf')] * (sugar+1)
    num[sugar] = 0


    for i in range(sugar, -1, -1):
        if i-5>=0:
            num[i-5] = min(num[i]+1, num[i-5])
        if i-3>=0:
            num[i-3] =  min(num[i]+1, num[i-3])

    if num[0] != float('inf'):
        print(num[0])
    else:
        print(-1)
solution()