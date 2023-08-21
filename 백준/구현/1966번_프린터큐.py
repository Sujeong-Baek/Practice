# https://www.acmicpc.net/problem/1966
from collections import deque
import sys
def solution():
    T = int(input())
    answer = []
    for _ in range(T):
        N, M = map(int, input().split())
        documents = list(map(int, sys.stdin.readline().split()))
        que = deque()
        count = 0
        for document, importance in enumerate(documents):
            que.append((document,importance))

        while que:
            current_d, current_i = que.popleft()
            if current_i < max(documents):
                que.append((current_d, current_i))
            else:
                documents.remove(current_i)
                count += 1
                if current_d == M:
                    answer.append(count)
                    break

    for a in answer:
        print(a)
solution()