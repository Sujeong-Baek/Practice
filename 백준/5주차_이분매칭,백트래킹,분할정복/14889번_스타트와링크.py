# https://www.acmicpc.net/problem/14889
from itertools import combinations
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

all_team = [i for i in range(N)]
min_diff = float('inf')
def calculate_total(team, S):
    total = 0
    for i in range(len(team)):
        for j in range(len(team)):
            total += S[team[i]][team[j]]
    return total
    
for start_team in combinations(all_team, N//2):
    link_team = list(set(all_team) -set(start_team))
    
    start_power = calculate_total(start_team, S)
    link_power = calculate_total(link_team, S)

    diff = abs(start_power-link_power)
    min_diff = min(min_diff, diff)

print(min_diff)


