# https://khu98.tistory.com/258
def solution():
    D, N, M = map(int, input().split())
    island = [int(input()) for _ in range(N)]
    island.sort()
    answer = 0
    left = 0
    right = D
    while left<=right:
        mid = (left+right)//2
        M_count = 0
        now = 0
        min_dis = D
        for i in island:
            if i-now >= mid:
                min_dis = min(min_dis, i-now)
                now = i
            else:
                M_count+=1
        
        min_dis = min(min_dis, D-now)

        if M_count > M:
            right = mid -1
        else:
            answer = max(answer, min_dis)
            left = mid + 1
    print(answer)
solution()