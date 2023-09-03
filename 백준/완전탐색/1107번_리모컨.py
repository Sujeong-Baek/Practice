# https://www.acmicpc.net/problem/1107
def can_press_channel(channel, broken_buttons):
    for ch in str(channel):
        if ch in broken_buttons:
            return False
    return True

def solution():
    target_channel = int(input())
    num_broken = int(input())
    if num_broken:
        broken_buttons = set(input().split())
    else:
        broken_buttons = set()

    min_press = abs(target_channel - 100)

    for channel in range(1000001):
        if can_press_channel(channel, broken_buttons):
            min_press = min(min_press, len(str(channel)) + abs(target_channel - channel))

    print(min_press)

solution()