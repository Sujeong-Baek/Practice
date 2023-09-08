# https://www.acmicpc.net/problem/4889
def solution():
    t = 1
    while True:
        S = input()
        if S[0] == '-':
            break
        
        stack = []
        ops = 0
        for s in S:
            if s == '{':
                stack.append('{')

            else:
                if stack:
                    stack.pop()
                else:
                    stack.append('{')
                    ops+=1

        print(f'{t}. {len(stack)//2+ops}')
        t += 1
solution()
