# https://www.acmicpc.net/problem/14888
n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_val = 1e9
max_val = -1e9

def dfs(i, res, add, sub, mul, div):
    global max_val, min_val
    if i == n:
        max_val = max(max_val, res)
        min_val = min(min_val, res)
        return
    
    if add:
        dfs(i+1, res+nums[i], add-1, sub, mul, div)
    if sub:
        dfs(i+1, res-nums[i], add, sub-1, mul, div)
    if mul:
        dfs(i+1, res*nums[i], add, sub, mul-1, div)
    if div:
        if res < 0:
            dfs(i+1, -(-res // nums[i]), add, sub, mul, div-1)  
        else:
            dfs(i+1, res // nums[i], add, sub, mul, div-1)  

dfs(1, nums[0], add, sub, mul, div)
print(int(max_val))
print(int(min_val))