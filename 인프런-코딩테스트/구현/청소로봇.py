def solution(n, moves):
    
    move2direction={'U':[-1,0],'R':[0,1],'L':[0,-1],'D':[1,0]}
    R=C=n
    r,c=0,0
    for move in moves:
        dr,dc=move2direction[move]
        nr=r+dr
        nc=c+dc
        if 0<=nr<R and 0<=nc<C:
            r=nr
            c=nc
    return [r,c]

moves='DDDRRRDDDDDDDLL'
print(solution(7,moves))