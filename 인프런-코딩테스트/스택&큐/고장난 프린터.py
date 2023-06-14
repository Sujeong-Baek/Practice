from collections import deque
def solution(nums):
    que=deque(nums)

    while que:
            
        for _ in range(2):
            if len(que)>1:
                que.popleft()

        if len(que)==1:
            return que[0]
        
        que.append(que.popleft())
    



print(solution([3, 1, 4, 5, 2, 6, 7]))
print(solution([10, 8, 3, 1, 4, 5, 2, 6, 7, 9]))
print(solution([10, 8, 3, 11, 12, 1, 4, 5, 2, 6, 7, 9]))
print(solution([10, 8, 3, 1, 4, 5, 2, 11, 13, 6, 7, 12, 9, 14]))
print(solution([1, 8, 6, 10, 4, 7, 2, 5, 3, 9]))