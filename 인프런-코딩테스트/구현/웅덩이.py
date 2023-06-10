def solution(nums):
    R=len(nums)
    C=len(nums[0])
    answer=0
    for r in range(R):
        for c in range(C):
            flag=True               
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr=r+dr
                nc=c+dc                
                if 0<=nr<R and 0<=nc<C and nums[r][c]>=nums[nr][nc]:                    
                    flag=False
                    break
            if flag:
                answer+=1     
    return answer

        

nums=[[10,20,50,30,20],[20,30,50,70,90],[10,15,25,80,35],[25,35,40,55,80],[30,20,35,40,90]]
print(solution(nums))