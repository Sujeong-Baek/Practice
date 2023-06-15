from collections import deque
def solution2(home):  
    quotient, remainder = divmod(home,5)
    return quotient + remainder if remainder < 3 else quotient-remainder+6



def solution(home):
    invited=[0]*10001
    Q=deque()
    Q.append(0)
    invited[0]=1
    L=0
    while Q:
        n=len(Q)
        for _ in range(n):
            num = Q.popleft()
            if num == home:
                return L
            for jump in [num-1, num+1, num+5]:
                if 0<jump<=10000 and invited[jump]==0:
                    Q.append(jump)
                    invited[jump]=1
        L+=1

print(solution(24))