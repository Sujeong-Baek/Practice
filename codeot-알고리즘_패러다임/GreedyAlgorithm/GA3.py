# 익중이네 밴드부는 매주 수요일 오후 6시에 합주를 하는데요. 
# 멤버들이 너무 상습적으로 늦어서, 1분에 1달러씩 내야 하는 벌금 제도를 도입했습니다.
# 그런데 마침 익중이와 친구 넷이 놀다가 또 지각할 위기입니다. 아직 악보도 출력해 놓지 않은 상황이죠.
# 어차피 같이 놀다 늦은 것이니 벌금을 다섯 명이서 똑같이 나눠 내기로 하고, 벌금을 가능한 적게 내는 방법을 고민해 보기로 합니다.
# 다섯 사람이 각각 출력해야 하는 페이지 수는 3장, 1장, 4장, 3장, 2장입니다. 
# 프린터는 한 대밖에 없고, 1장을 출력하기 위해서는 1분이 걸립니다.
# 현재 순서대로 출력한다면, 아래와 같이 총 39달러의 벌금을 내야 합니다.

# 출력할 페이지 수가 담긴 리스트 pages_to_print를 파라미터로 받고 
# 최소 벌금을 리턴해 주는 함수 min_fee를 Greedy Algorithm으로 구현하세요.


def min_fee(pages_to_print):
    # 여기에 코드를 작성하세요
    sorted_list=sorted(pages_to_print)
    total_fee=0
    for i in range(len(pages_to_print)):
        total_fee+=sorted_list[i]*(len(pages_to_print)-i)
    return total_fee
    

# 테스트 코드
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
