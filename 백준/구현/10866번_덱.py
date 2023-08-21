# https://www.acmicpc.net/problem/10866
def solution():
    N = int(input())
    command = [list(map(str, input().split())) for _ in range(N)]
    deque = []
    answer = []

    for c in command:
        if c[0] == 'push_back':
            deque.append(c[1])
        
        elif c[0] == 'push_front':
            temp = [c[1]]
            temp.extend(deque)
            deque = temp

        elif c[0] == 'front':
            if deque:
                answer.append(int(deque[0]))
            else:
                answer.append(-1)

        elif c[0] == 'back':
            if deque:
                answer.append(int(deque[-1]))
            else:
                answer.append(-1)

        elif c[0] == 'size':
            answer.append(len(deque))

        elif c[0] == 'empty':
            if deque:
                answer.append(0)
            else:
                answer.append(1)

        elif c[0] == 'pop_front':
            if deque:
                answer.append(deque[0])
                deque = deque[1:]
            else:
                answer.append(-1)

        elif c[0] == 'pop_back':
            if deque:
                answer.append(deque[-1])
                deque = deque[:-1]
            else:
                answer.append(-1)

    for a in answer:
        print(a)
            
solution()