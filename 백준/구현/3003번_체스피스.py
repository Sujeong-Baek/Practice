#https://www.acmicpc.net/problem/3003
def solution():
    Original = [1,1,2,2,2,8]
    white = list(map(int, input().split()))
    answer = []
    for O, w in zip(Original, white):
        answer.append(O-w)
    
    for a in answer[:-1]:
        print(a, end=' ')
    print(answer[-1])
    
solution()