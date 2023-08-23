# https://www.acmicpc.net/problem/11723
import sys
sys.setrecursionlimit(10**6)
def solution(): 
    N = int(input())
    S = 0

    for _ in range(N):
        c = sys.stdin.readline().split()
        if c[0] == 'add':
            x = int(c[1])
            S |= (1 << (x - 1))

        elif c[0] == 'remove':
            x = int(c[1])
            S &= ~(1 << (x - 1))

        elif c[0] == 'check':
            x = int(c[1])
            if S & (1 << (x - 1)):
                print(1)
            else:
                print(0)

        elif c[0] == 'toggle':
            x = int(c[1])
            S ^= (1 << (x - 1))

        elif c[0] == 'all':
            S = (1 << 20) - 1

        elif c[0] == 'empty':
            S = 0

solution()


