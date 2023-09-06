# https://www.acmicpc.net/problem/2143
from bisect import bisect_right, bisect_left
import sys
input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

A_sum = []
for i in range(n):
    s=0
    for j in range(i, n):
        s += A[j]
        A_sum.append(s)
B_sum = []
for i in range(m):
    s = 0
    for j in range(i, m):
        s += B[j]
        B_sum.append(s)

A_sum.sort()
answer = 0
for b in B_sum:
    lower = bisect_left(A_sum, T-b)
    upper = bisect_right(A_sum, T-b)
    answer += upper-lower
print(answer)

