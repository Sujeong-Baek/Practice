# https://www.acmicpc.net/problem/10799
def solution():
    S = list(map(str, input()))
    answer = 0
    stack = []
    for i, s in enumerate(S):
        if s =='(':
            stack.append(s)
        else:
            stack.pop()
            if S[i-1] == '(':
                answer += len(stack) 
            else:
                answer += 1
    print(answer)
solution()
