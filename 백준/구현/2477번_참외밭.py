# https://www.acmicpc.net/problem/2477
from collections import defaultdict
def solution():
    melon = int(input())
    field = [list(map(int, input().split())) for _ in range(6)]
    a = 0
    b = 0
    direction2length = defaultdict(list)
    for d, l in field:
        direction2length[d].append(l)
    
    for i, (d, l) in enumerate(field):
        if len(direction2length[d]) == 2 and len(direction2length[field[i-1][0]]) == 2 and len(direction2length[field[(i+1)%6][0]]) == 2:
            if b == 0:
                b = l
            else:
                b *= l

        elif len(direction2length[d]) == 1:
            if a == 0:
                a = l
            else:
                a *= l

    print((a-b)*melon) 

solution()