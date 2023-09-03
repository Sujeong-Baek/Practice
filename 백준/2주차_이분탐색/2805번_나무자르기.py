# https://www.acmicpc.net/problem/2805
def solution():
    T, NEED = map(int, input().split())
    Trees = list(map(int, input().split()))
    left = 0
    right = max(Trees)

    while left < right:
        mid = (left+right)//2
        total = sum([tree-mid for tree in Trees if tree>=mid])

        if total < NEED:
            right = mid - 1
        else:
            left = mid + 1

    total = sum([tree-left for tree in Trees if tree>left])
    if total<NEED:
        print(left-1)
    else:
        print(left)
  
solution()