# https://www.acmicpc.net/problem/3986
def solution():
    N = int(input())
    answer = 0
    for _ in range(N):
        report = list(map(str, input()))
        stack = []
        for r in report:
            if stack and stack[-1] == r:
                stack.pop()
            else:
                stack.append(r)
        
        if not stack:
            answer += 1
    print(answer)

solution()