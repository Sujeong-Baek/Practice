# n번째 피보나치 수를 찾아주는 함수 fib_memo을 작성해 보세요.
# fib_memo는 꼭 memoization 방식으로 구현하셔야 합니다!
def fib_memo(n, cache):
    # 여기에 코드를 작성하세요


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트 코드
print(fib(10))
print(fib(50))
print(fib(100))