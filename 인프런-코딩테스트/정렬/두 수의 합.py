def solution(target, nums):
    answer=[0,0]
    nums.sort()
    left=0
    right=len(nums)-1
    while left<right:
        total=nums[left]+nums[right]
        
        if total==target:
            return [nums[left], nums[right]]
        
        if total < target:
            left+=1
        
        else:
            right-=1
    return answer

target=24
nums=[7,5,12,20]
print(solution(target, nums))