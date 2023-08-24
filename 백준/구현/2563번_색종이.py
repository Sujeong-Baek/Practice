# https://www.acmicpc.net/problem/2563
def solution():
    N = int(input())
    papers = [list(map(int, input().split())) for _ in range(N)]
    white = [[False]*101 for _ in range(101)]

    for x1, y1 in papers:
        for x2 in range(10):
            for y2 in range(10):
                white[x1+x2][y1+y2] = True

    print(sum(sum(w) for w in white))
                

solution()