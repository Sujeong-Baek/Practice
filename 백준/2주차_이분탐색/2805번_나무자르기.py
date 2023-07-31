# https://www.acmicpc.net/problem/2805
def solution():
    T, NEED = map(int, input().split())
    Trees = list(map(int, input().split()))
    Trees.sort()
    left = 0
    right = Trees[-1]

    while left < right:
        mid = (left+right)//2
        total = sum([tree-mid for tree in Trees if tree>=mid])
        if total < NEED:
            right = mid - 1
        else:
            left = mid + 1
    total = sum([tree-right for tree in Trees if tree>=right])
    if total<NEED:
        print(right-1)
    else:
        print(right)
  
solution()