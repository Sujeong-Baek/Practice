# n번째 피보나치 수를 찾아주는 함수 fib_tab을 작성해 보세요.
# fib_tab는 꼭 tabulation 방식으로 구현하셔야 합니다!
def fib_tab(n):
    # 여기에 코드를 작성하세요
    fib_list=[0,1,1]

    for i in range(3,n+1):
        fib_list.append(fib_list[i-1]+fib_list[i-2])
    return fib_list[n]
    

# 테스트 코드
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))