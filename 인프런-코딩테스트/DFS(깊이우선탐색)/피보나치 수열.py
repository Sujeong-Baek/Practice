def solution(n):
    if n== 1:
        return 1
    if n == 2:
        return 1
    
    return solution(n-1)+ solution(n-2)
