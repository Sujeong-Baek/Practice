# https://www.acmicpc.net/problem/1193
def solution():
    X = int(input())

    x = 1
    n = 1
   
    while x <= (X-n):
        x += n
        n += 1

    if n%2 == 0:
        print(f'{1+X-x}/{n-X+x}')
    else:
        print(f'{n-X+x}/{1+X-x}')

solution()