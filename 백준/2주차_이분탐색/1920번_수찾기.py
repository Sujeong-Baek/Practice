# https://www.acmicpc.net/problem/1920
def solution():
    A = int(input())
    Anums = list(map(int, input().split()))
    Anums.sort()
    M = int(input())
    Mnums = list(map(int, input().split()))
    answer = []
    for num in Mnums:
        answer.append(serch(num, Anums))

    for a in answer:
        print(a)
    
def serch(num, Anums):
    s = 0
    e = len(Anums)-1

    while s <= e:
        mid = (s+e)//2
        if Anums[mid] == num:
            return 1
        if Anums[mid] > num:
            e = mid-1
        else:
            s = mid+1
    return 0

solution()