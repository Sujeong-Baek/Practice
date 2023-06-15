from collections import deque
def solution(board):
    answer=0
    for r in range(5):
        for c in range(5):
            if board[r][c]==1:
                answer+=1
                bfs(board,r,c)
    return answer


def bfs(board,r,c):
    Q=deque()
    Q.append([r,c])
    board[r][c]=0

    while Q:
        r, c = Q.popleft()

        for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
            nr= r+dr
            nc= c+dc
            if 0<=nr<5 and 0<=nc<5 and board[nr][nc]==1:
                Q.append([nr,nc])
                board[nr][nc]=0


print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))