# https://www.acmicpc.net/problem/2613
def solution():
    B, G = map(int, input().split())
    balls = list(map(int, input().split()))
    left = max(balls)
    right = sum(balls)
    answer = right

    while left <= right:
        mid = (left+right)//2
        
        total = 0
        group = 0
        for ball in balls:
            if total+ball > mid:
                group+=1
                total = 0
            total+=ball
        group+=1
        if group>G:
            left = mid +1
        else:
            right = mid -1
            answer = min(mid, answer)


    total = balls[0]
    groups = [1]*G
    idx = 0
    for ball in balls[1:]: 
        total += ball
        if total > answer:
            idx+=1
            total = ball
        elif sum(groups)<B:
            groups[idx] += 1
    print(answer)
    print(' '.join(map(str, groups)))

solution()