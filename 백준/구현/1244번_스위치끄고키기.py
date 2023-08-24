# https://www.acmicpc.net/problem/1244
def solution():
    N = int(input())
    switch = list(map(int, input().split()))
    M = int(input())
    students = [list(map(int, input().split())) for _ in range(M)]
    
    for gender, number in students:
        if gender == 1:
            boy_on_off(N, switch, number)
        else:
            girl_on_off(N, switch, number)

    for i, s in enumerate(switch, 1):
        if i % 20 > 0:
            print(s, end=' ')
        else:
            print(s)


def boy_on_off(N, switch, number):
    for i in range(number-1, N, number):
        switch[i] = 1 - switch[i]
     

def girl_on_off(N, switch, number):
    idx = number-1
    left = idx - 1
    right = idx + 1
   
    switch[idx] = 1 - switch[idx]
    
    while left >= 0 and right < N:
        if switch[left] == switch[right]:
            switch[left] = 1 - switch[left]
            switch[right] = 1 - switch[right]
            left -= 1
            right += 1

        else:
            break

solution()