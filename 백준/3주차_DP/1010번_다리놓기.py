# https://www.acmicpc.net/problem/1010
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def combination(m, n):
    return factorial(m) // (factorial(n) * factorial(m-n))

def solution():
    T = int(input()) # 테스트 케이스 수

    for _ in range(T):
        N, M = map(int, input().split())
        print(combination(M, N))

solution()
