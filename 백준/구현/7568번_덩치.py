# https://www.acmicpc.net/problem/7568
def solution():
    N = int(input())
    sizes = [list(map(int, input().split())) for _ in range(N)]
    answer = []
    for w1, h1 in sizes:
        count = 0
        for w2, h2 in sizes:
            if w1 < w2 and h1 < h2:
                count += 1
        answer.append(count+1)

    for a in answer:
        print(a, end=' ')



solution()