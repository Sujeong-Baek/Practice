def solution(board):
    answer=[]
    for r in range(5):
        for c in range(5):            
            if board[r][c] == 1:  
                count=1
                answer.append(dfs(board,r,c,count))
    return answer


def dfs(board, r, c,count):
    board[r][c]=0
    for dr, dc in [[0,1],[0,-1],[1,0],[-1,0]]:
        nr= dr+r
        nc= dc+c
        if 0<=nr<5 and 0<=nc<5 and board[nr][nc]==1:         
            count = dfs(board,nr,nc,count+1)
    return count

print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))