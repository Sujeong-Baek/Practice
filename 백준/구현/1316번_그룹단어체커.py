# https://www.acmicpc.net/problem/1316
def solution():
    N = int(input())
    words = [list(map(str, input())) for _ in range(N)]
    answer = 0
    for word in words:
        answer += check_word(word)
    print(answer)

def check_word(word):
    temp = word[0]
    ws = [word[0]]
    for w in word[1:]:
        if temp == w:
            continue
        if w not in ws:
            temp = w
            ws.append(w)
        else:
            return 0
    return 1

solution()