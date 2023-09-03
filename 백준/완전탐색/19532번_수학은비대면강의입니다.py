# https://www.acmicpc.net/problem/19532
def solution():
    A, B, C, D, E, F = map(int, input().split())

    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if A*x + B*y == C and D*x + E*y == F:
                print(x, end=' ')
                print(y)
                break

solution()