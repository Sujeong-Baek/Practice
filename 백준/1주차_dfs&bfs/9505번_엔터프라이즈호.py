# https://www.acmicpc.net/problem/9505
from collections import defaultdict
import sys
import heapq
input = sys.stdin.readline
def solution():
    T = int(input())
    for _ in range(T):
        K, W, H = map(int, input().split())

        K2time = defaultdict(int)
        for _ in range(K):
            k, t = map(str, input().split())
            K2time[k]=int(t)

        board = [input().rstrip() for _ in range(H)]
        que = []
        distances = [[float('inf')] * W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if board[i][j] == 'E':
                    heapq.heappush(que, (0, i, j))
                    distances[i][j] = 0

        while que:
            current_dist, r, c = heapq.heappop(que)
            if r in [0, H-1] or c in [0, W-1]:
                print(distances[r][c])
                break

            for dr, dc in [[1,0], [-1,0], [0,1],[0,-1]]:
                nr, nc = dr+r, dc+c

                if 0<= nr < H and 0<= nc < W and distances[nr][nc] > current_dist + K2time[board[nr][nc]]:
                    distances[nr][nc] = current_dist + K2time[board[nr][nc]]
                    heapq.heappush(que, (distances[nr][nc], nr, nc))
solution()
