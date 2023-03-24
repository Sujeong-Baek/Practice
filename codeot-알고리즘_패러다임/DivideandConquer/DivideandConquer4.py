# partition 함수 설명 영상을 토대로 partition 함수를 작성하세요.
# partition 함수는 리스트 my_list, 그리고 partition할 범위를 나타내는 인덱스 start와 인덱스 end를 파라미터로 받습니다. 
# my_list의 값들을 pivot 기준으로 재배치한 후, pivot의 최종 위치 인덱스를 리턴해야 합니다.

# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 여기에 코드를 작성하세요




# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 여기에 코드를 작성하세요

# # 테스트 코드 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 코드 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)
