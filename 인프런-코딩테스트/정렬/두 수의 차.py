def solution(nums):
    nums.sort()
    answer=[]
    min_diff=float('inf')
    for i in range(1, len(nums)):
        num_diff=nums[i]-nums[i-1]
        if num_diff< min_diff:
            min_diff=num_diff
            answer.clear()
            answer.append([nums[i-1],nums[i]])
        elif num_diff==min_diff:
            answer.append([nums[i-1],nums[i]])
    return answer

nums=[2,4,3,1,5,7,8,12,13,15,23]
print(solution(nums))