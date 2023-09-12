# https://www.acmicpc.net/problem/1120
import sys
input =  sys.stdin.readline
def solution():
    A, B = map(str, input().split())
    min_diff = len(B)+1
    
    for i in range(len(B)-len(A)+1):
        count = 0
        for idx, b in enumerate(B[i:i+len(A)]):
            if A[idx] != b:
                count += 1
        min_diff = min(min_diff, count)
    print(min_diff)
    
solution()