# https://www.acmicpc.net/problem/1076
def solution():
    colors = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4, 'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}
    data = [str(input()) for _ in range(3)]
    answer = 0
    for i, color in enumerate(data):
        if i == 0:
            answer += colors[color]*10
        elif i == 1:
            answer += colors[color]
        else:
            answer *= (10**colors[color])
    print(answer)
solution()