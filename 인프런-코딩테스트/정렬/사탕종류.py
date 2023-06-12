def solution(nums):
    nums.sort()
    answer=1
    for i in range(len(nums[:-1])):
        if nums[i] != nums[i+1]:
            answer+=1
        
    return min(answer, len(nums)//2)

nums=[12,23,11,3,5,23,23,23,23,23,23,23]
print(solution(nums))