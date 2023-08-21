# https://www.acmicpc.net/problem/2108
from collections import Counter
import sys
def solution():
    N = int(input())
    nums = [int(sys.stdin.readline()) for _ in range(N)]
    nums.sort()

    answer = []
    answer.append(round(sum(nums)/len(nums)))
    answer.append(nums[(len(nums)-1)//2])

    num2count = Counter(nums).most_common()
    max_count = num2count[0][1]
    max_count_nums = []
    for num in num2count:
        if max_count == num[1]:
            max_count_nums.append(num[0])
        else:
            break

    if len(max_count_nums)>1:
        answer.append(max_count_nums[1])
    else:
        answer.append(max_count_nums[0])
 
    num1 = abs(nums[-1]-nums[0])
    answer.append(num1)

    for a in answer:
        print(a)
    

solution()