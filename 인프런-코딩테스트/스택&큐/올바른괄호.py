def solution(s):

    stack=[]

    for pare in s:
        if pare == '(':
            stack.append(pare)
        else:
            if stack:
                stack.pop()
            else: 
                return "NO"

    return 'YES' if not stack else 'NO'


print(solution("((()))()"))
print(solution("(()(()"))
print(solution("()())"))
print(solution("())("))
print(solution("((())))()("))
