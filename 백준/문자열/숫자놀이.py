# https://www.acmicpc.net/problem/1755
def solution():
    n, m = map(int, input().split())
    nums = []
    num2eng = {'0':'zero', '1':'one', '2':'two', '3':'tree', '4':'four', '5':'five', '6':'six','7':'seven','8':'eight','9':'nine'}
    eng2num = {}
    answer = []
    for num, eng in num2eng.items():
        eng2num[eng] = num

    for num in range(n, m+1):
        if len(str(num))>1:
            a,b = map(str, str(num))
            nums.append([num2eng[a], num2eng[b]])
        else:
            a = str(num)
            nums.append([num2eng[a]])

    nums.sort()

    for num in nums:
        a = ''
        for n in num:
            a += eng2num[n]
        answer.append(int(a))

    for i in range(len(answer)):
        if (i+1)%10 == 0:
            print(answer[i])
        else:
            print(answer[i], end=' ')
solution()
