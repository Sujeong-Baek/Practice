def solution(moves):    
    direction=[[-1,0], [0,1], [1,0], [0,-1]]
    r,c=0,0
    face=1
    for move in moves:
        if move == 'R':
            face= (face+1)%4     
            continue
        if move == 'L':
            face=(face-1)%4
            continue
        dr,dc=direction[face]
        r+=dr
        c+=dc

    return [r,c]

moves='GGLLLGLGGG'
print(solution(moves))
