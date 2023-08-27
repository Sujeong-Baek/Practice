# https://www.acmicpc.net/problem/1780
def solution():
    N = int(input())
    paper = [list(map(int, input().split())) for _ in range(N)]
    count = {-1:0, 0:0, 1:0}
    
    def check(r, c, size):
        value = paper[r][c]
        for i in range(r, r+size):
            for j in range(c, c+size):
                if paper[i][j] != value:
                    return False
        return True
    
    def divide_conquer(r, c, size):

        if check(r, c, size):
            count[paper[r][c]]+=1
            return
        
        new_size = size//3
        for i in range(3):
            for j in range(3):
                divide_conquer(r + i*new_size, c + j*new_size, new_size)

    divide_conquer(0,0,N)
    for c in count:
        print(count[c])


solution()