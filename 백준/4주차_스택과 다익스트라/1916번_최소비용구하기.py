# https://www.acmicpc.net/problem/1916
from collections import defaultdict
import heapq, sys
sys.setrecursionlimit(10**6)
def solution():
    N = int(input())
    M = int(input())

    Buses = defaultdict(list)
    for _ in range(M):
        s, e, c = map(int, sys.stdin.readline().split())
        Buses[s].append((e,c))

    start, end = map(int, input().split())

    costs = [float('inf')] * (N+1)
    que = []
    heapq.heappush(que, (0, start))
    costs[start] = 0

    while que:
        current_cost, current_city = heapq.heappop(que)
        if costs[current_city] < current_cost:
            continue

        for next_city, next_cost in Buses[current_city]:
            if costs[next_city] > current_cost + next_cost:
                costs[next_city] = current_cost + next_cost
                heapq.heappush(que, (current_cost+next_cost, next_city))
    print(costs[end])

solution()