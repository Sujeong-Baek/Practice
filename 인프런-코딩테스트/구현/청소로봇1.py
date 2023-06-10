def solution(moves):
    move2direction={'U':[-1,0],'R':[0,1],'L':[0,-1],'D':[1,0]}
    nr,nc=0,0
    for move in moves:
        dr,dc=move2direction[move]
        nr+=dr
        nc+=dc
    return [nr, nc]

moves='RRRDDDLU'
print(solution(moves))