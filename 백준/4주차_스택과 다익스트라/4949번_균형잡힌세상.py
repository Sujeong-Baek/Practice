# https://www.acmicpc.net/problem/4949
def solution():
    answer = []
    while True:
        s = input()
        if s=='.': 
            break
        else:
            S = list(map(str, s))
            answer.append(search_yes_no(S))
    for a in answer:
        print(a)
    

def search_yes_no(s):
    match = {')':'(', ']':'['}
    stack=[]
    for el in s:
        if el in '([':
            stack.append(el)

        elif el in ')]':
            if stack and match[el] == stack[-1]:
                stack.pop()
            else:
                return 'no'
            
    return 'no' if stack else 'yes'

solution()