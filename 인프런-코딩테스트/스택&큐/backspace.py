def solution(s):
    
    stack=[]
    for el in s:
        if el == '#':
            stack.pop()

        else:
            stack.append(el)


    return ''.join(stack)


print(solution("abc##ec#ab"))
print(solution("kefd#ef##s##"))
print(solution("teac#cher##er"))
print(solution("englitk##shabcde##ff##ef##ashe####"))
print(solution("itistime####gold"))


