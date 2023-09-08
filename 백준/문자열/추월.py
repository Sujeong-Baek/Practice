# https://www.acmicpc.net/problem/2002
from collections import defaultdict
import sys
input = sys.stdin.readline
def solution():
    t =int(input())
    answer = 0
    car2level=defaultdict(int)
    for i in range(t):
        car = input().strip()
        car2level[car]=i

    cars = [input().strip() for _ in range(t)]

    for i in range(t-1):
        for j in range(i+1,t):
            if car2level[cars[i]] > car2level[cars[j]]:
                answer+=1
                break
    print(answer)
solution()