# https://www.acmicpc.net/problem/1475
def solution():
    N = list(map(int, input()))
    count = [0]*10
    
    for n in N:
        if n == 6 or n == 9:
            if count[6]<count[9]:
                count[6] += 1
            else:
                count[9] += 1
        else:
            count[n]+=1

    print(max(count))

solution()