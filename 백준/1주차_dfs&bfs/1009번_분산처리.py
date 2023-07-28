# https://www.acmicpc.net/problem/1009
import sys
def solution():
    N = int(input())
    answer = []
    data =[[1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1], [10]]
    for _ in range(N):
        n1, n2 =  map(int, sys.stdin.readline().split())
        answer.append(data[(n1%10)-1][(n2%len(data[(n1%10)-1]))-1])
    
    for a in answer:
        print(a)

solution()