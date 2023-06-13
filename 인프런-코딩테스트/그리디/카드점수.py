def solution(nums, k):
    total= sum(nums)
    lenth=len(nums)
    score=sum(nums[:lenth-k])
    min_score= score
    start=0

    for end in range(lenth-k, lenth):
        score +=nums[end]-nums[start]
        min_score=min(score, min_score)
        start+=1
    return total-min_score



print(solution([2, 3, 7, 1, 2, 1, 5], 4))
print(solution([1, 2, 3, 5, 6, 7, 1, 3, 9], 5))
print(solution([1, 30, 3, 5, 6, 7], 3))
print(solution([1, 2, 15, 3, 6, 7, 8, 9], 5))
print(solution([12, 5, 6, 12, 34, 35, 13, 3, 7, 8, 9], 7))
