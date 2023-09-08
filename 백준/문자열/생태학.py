# https://www.acmicpc.net/problem/4358
from collections import defaultdict
import sys
input = sys.stdin.readline
def solution():
    tree2count = defaultdict(int)
    total = 0
    while True:
        tree = input().strip()
        if not tree:
            break
        tree2count[tree]+=1
        total += 1

    for tree in sorted(tree2count, key = lambda x:x):
        print(f'{tree} {tree2count[tree]/total*100:.4f}')

solution()
