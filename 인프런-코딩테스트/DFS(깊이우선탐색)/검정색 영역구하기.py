def solution(board):
    answer=0
    for r in range(5):
        for c in range(5):
            if board[r][c]==1:
                answer+=1
                dfs(board,r,c)
    return answer

def dfs(board,r,c):
    board[r][c]=0
    R=C=5
    for dr, dc in [[0,1],[0,-1],[1,0],[-1,0]]:
        nr=dr+r
        nc=dc+c
        if 0<=nr<R and 0<=nc<C and board[nr][nc]==1:
            dfs(board, nr, nc)



print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))