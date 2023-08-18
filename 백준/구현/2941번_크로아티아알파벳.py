# https://www.acmicpc.net/problem/2941
def solution():
    change = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    word = input()
    answer = 0
    idx = 0
    while idx < len(word):

        if idx+2 <= len(word) and word[idx:idx+2] in change:
            idx += 2
            answer += 1

        elif idx+3 <= len(word) and word[idx:idx+3] in change:
            idx += 3
            answer += 1

        else:
            idx += 1
            answer += 1

    print(answer)
solution()