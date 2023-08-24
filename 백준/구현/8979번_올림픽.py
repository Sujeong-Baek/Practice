# https://www.acmicpc.net/problem/8979
def solution():
    N, K = map(int, input().split())

    medals = [list(map(int, input().split())) for _ in range(N)]
    medals = sorted(medals, key = lambda x : (-x[1],-x[2],-x[3]))

    rank = 1
    count = 0
    for i, (c, g, s, b) in enumerate(medals):
        if c == K:
            if i>0 and medals[i-1][1:] == [g, s, b]:
                print(rank -1)
            else:
                print(rank+count)
            break
        
        if i>0 and medals[i-1][1:] == [g, s, b]:
            count += 1
        else:
            rank += (1+ count)
            count = 0
        
solution()