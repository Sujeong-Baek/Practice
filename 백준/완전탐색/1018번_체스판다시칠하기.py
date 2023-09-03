# https://www.acmicpc.net/problem/1018
def solution():
    n, m = map(int, input().split())
    board = [list(map(str, input())) for _ in range(n)]
    answer = float('inf')
    for r in range(n-8+1):
        for c in range(m-8+1):
            cutted_board = [board[r+i][c:c+8 ]for i in range(8)]
            answer = min(answer, check_board(cutted_board))
    print(answer)
            
def check_board(board):

    white = 0
    black = 0

    for r in range(8):
        for c in range(8):
            if (r+1)%2 != 0 and (c+1)%2 != 0:
                if board[r][c] =='B':
                    white += 1
                else:
                    black += 1

            elif (r+1)%2 == 0 and (c+1)%2 == 0:
                if board[r][c] =='B':
                    white += 1
                else:
                    black += 1

            elif (r+1)%2 != 0 and (c+1)%2 == 0:
                if board[r][c] =='W':
                    white += 1
                else:
                    black +=1
            else:
                if board[r][c] == 'W':
                    white += 1
                else:
                    black += 1

           

    return min(white, black)

solution()