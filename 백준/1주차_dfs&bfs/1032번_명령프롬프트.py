# https://www.acmicpc.net/problem/1032
def solution():

    N = int(input())
    data = [str(input()) for _ in range(N)]
    print(data)
    answer = ''
    for chars in zip(*data):
        if len(set(chars)) > 1 :
            answer+='?'
        else:
            answer += chars[0]
    print(answer)
solution()
