# https://www.acmicpc.net/problem/4673
def solution():
    not_self = []
    for num in range(1, 10000):
        n = div(num)
        not_self.append(n)

    for num in range(1, 10000):
        if num not in not_self:
            print(num)    

def div(num):
    answer = num
    n = 10**(len(str(num)))
    while n > 0:
        a, b = divmod(num, n)
        answer += a
        num = b
        n //= 10
    return answer

solution()
