# https://www.acmicpc.net/problem/1753
from collections import defaultdict
import heapq, sys
sys.setrecursionlimit(10**6)
def solution():
    V, E = map(int, input().split())
    K =int(input())

    distance = [float('inf')] * (V+1)
    distance[K] = 0
    
    graph = defaultdict(list)
    for _ in range(E):
        n1, n2, w = map(int, sys.stdin.readline().split())
        graph[n1].append((n2, w))
    
    que = []
    heapq.heappush(que, (0,K))

    while que:
        dist, current = heapq.heappop(que)

        if distance[current] < dist:
            continue

        for neighber, w in graph[current]:
            if distance[neighber] > dist + w:
                distance[neighber] = dist + w
                heapq.heappush(que, (dist+w, neighber))
   
    for d in distance[1:]:
        print(d if d != float('inf') else 'INF')
solution()