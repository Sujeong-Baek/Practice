# https://www.acmicpc.net/problem/9576
import sys
def solution():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        requests = [list(map(int, input().split())) for _ in range(M)]
        requests = sorted(requests, key = lambda x : x[1])
        visited = [False] * (N+1)
        count = 0

        for a, b in requests:
            for i in range(a, b+1):
                if visited[i] == False:
                    visited[i] = True
                    count+=1
                    break

        print(count)




def solution2():
    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())
        requests = [list(map(int, input().split())) for _ in range(M)]
        sorted_students = sorted([(b - a, student) for student, (a, b) in enumerate(requests, 1)])
        adj = [[] for _ in range(M+1)]
        
        for _, student in sorted_students:
            a, b = requests[student - 1]
            for book in range(a, b+1):
                adj[student].append(book)

        visited = [False] * (M+1)
        match_book = [0] * (N+1)
        match_student = [0] * (M+1)

        def bfs(student):
            if visited[student]:
                return False
            visited[student] = True

            for book in adj[student]:
                if match_book[book] == 0 or bfs(match_book[book]):
                    match_book[book] = student
                    match_student[student] = book
                    return True
            return False
        
        count = 0
        for _, student in sorted_students:
            visited = [False] * (M+1)
            if bfs(student):
                count += 1

        print(count)
