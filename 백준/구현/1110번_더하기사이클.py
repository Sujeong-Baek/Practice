# https://www.acmicpc.net/problem/1110
def solution():
    number = input()
    numbers =[]
    if len(number) == 1:
        numbers.append(0)
        numbers.append(int(number))
    else:
        numbers = list(map(int, number))

    new_numbers = [numbers[1], sum(numbers)%10]
    count = 1
    while new_numbers != numbers:
        count+=1
        new_numbers[0], new_numbers[1] = new_numbers[-1], sum(new_numbers)%10
    print(count)
solution()