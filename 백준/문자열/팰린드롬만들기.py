# https://www.acmicpc.net/problem/1254
def solution():
    S = input()
    
    for i in range(len(S)):
        if S[i:] == S[i:][::-1]:
            print(len(S[i:])+(i*2))
            break

solution()