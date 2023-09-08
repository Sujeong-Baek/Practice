# https://www.acmicpc.net/problem/2609
def solution():
    a, b = map(int, input().split())
    g = gcd(a, b)
    l = lcm(a*b, g)
    print(g)
    print(l)

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(ab, gcd):
    return ab//gcd

solution()