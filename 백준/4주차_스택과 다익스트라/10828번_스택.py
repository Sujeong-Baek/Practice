# https://www.acmicpc.net/problem/10828
def solution():
    N = int(input())

    command = [list(map(str, input().split())) for _ in range(N)]
    stack = []
    for c in command:
        if c[0] == 'push':
            stack.append(int(c[1]))
        
        elif c[0] == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)

        elif c[0] == 'pop':
            if stack:
                print(stack[-1])
                stack=stack[:-1]
            else:
                print(-1)

        elif c[0] == 'size':
            print(len(stack))

        elif c[0] == 'empty':
            if stack:
                print(0)
            else:
                print(1)
    
solution()