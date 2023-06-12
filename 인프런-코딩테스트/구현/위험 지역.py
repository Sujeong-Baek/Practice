def solution(board):
    R=C=5
    answer=0
    for r in range(R):
        for c in range(C):
            if board[r][c] == 1:
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<R and 0<=nc<C and board[nr][nc]==0:
                       answer+=1
                       board[nr][nc]=2

    return answer

board=[[1,0,0,1,0],[0,1,0,0,0],[0,1,0,1,0],[0,0,0,0,0],[0,1,0,0,0]]
print(solution(board))

nums=[[1,2],[2,4],[1,5],[3,5],[1,3],[2,5]]
nums.sort(key=lambda x: (x[0], x[1]))
print(nums)