# https://www.acmicpc.net/problem/1934
import sys
input = sys.stdin.readline
def solution():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        g = gcd(a, b)
        l = lcm(a*b, g)
        print(l)

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(ab, g):
    return ab//g

solution()