# https://www.acmicpc.net/problem/1100
def solution():
    board = [list(map(str, input())) for _ in range(8)]
    answer = 0
    for r in range(8):
        for c in range(8):
            if r%2 == 0 and c%2 == 0 and board[r][c]=='F':
                answer += 1

            elif r%2 == 1 and c%2 == 1 and board[r][c]=='F':
                answer+=1
    print(answer)
solution()