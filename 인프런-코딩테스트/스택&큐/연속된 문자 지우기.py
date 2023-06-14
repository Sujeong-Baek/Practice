def solution(s):
    stack=[]

    for el in s:
        if stack and stack[-1]==el:
            stack.pop()
        else:
            stack.append(el)
    return ''.join(stack)


print(solution("acbbcaa"))
print(solution("bacccaba"))
print(solution("aabaababbaa"))
print(solution("bcaacccbaabccabbaa"))
print(solution("cacaabbc"))
