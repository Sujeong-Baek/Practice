# https://www.acmicpc.net/problem/1238
from collections import defaultdict
import sys, heapq
sys.setrecursionlimit(10**6)
def solution():
    N, M, X = map(int, input().split())
    
    graph = defaultdict(list)
    for _ in range(M):
        s, e, t = map(int, sys.stdin.readline().split())
        graph[s].append((t, e))

    answer = []
    for i in range(1, N+1):
        answer.append(dijkstra(N, graph, X, i) + dijkstra(N, graph, i, X))
    print(max(answer))

def dijkstra(N, graph, start, end):

    distance = [float('inf')] * (N+1)
    distance[start] = 0

    que = []
    heapq.heappush(que, (0, start))

    while que:
        current_time, current_home = heapq.heappop(que)

        if distance[current_home] < current_time:
            continue
            
        for next_time, next_home in graph[current_home]:
            if distance[next_home] > current_time + next_time:
                distance[next_home] = current_time + next_time
                heapq.heappush(que, (current_time+next_time, next_home))

    return distance[end]

solution()

