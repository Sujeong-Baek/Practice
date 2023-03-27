# 그런데 quicksort 함수에 필수로 start와 end 파라미터를 넘겨줘야 한다는 게 조금 거슬리네요. 
# 테스트를 할 때 만큼은 아래처럼 깔끔하게 작성하고 싶은데요.
# 테스트 코드
# test_list = [9, 5, 1, 5, 2, 8, 2, 7, 1, 3, 6, 2, 4, 7, 10, 11, 4, 6]
# quicksort(test_list) # start, end 파라미터 없이 호출
# print(test_list)

# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    my_list[index1],my_list[index2]=my_list[index2],my_list[index1]


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    pivot=my_list[end]
    bigger_index=start
    for i in range(start,end):
        if my_list[i]<pivot:
            swap_elements(my_list,bigger_index,i)
            bigger_index+=1
    swap_elements(my_list,bigger_index,end)
    return bigger_index


def quicksort(my_list, start=0, end=None):
    # 여기에 코드를 작성하세요
    if end==None:
        end=len(my_list)-1
    if start>=end:
        return
    pivot=partition(my_list, start, end)
    quicksort(my_list,pivot+1, end)
    quicksort(my_list,start, pivot-1)
    

# 테스트 코드 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1) # start, end 파라미터 없이 호출
print(list1)

# 테스트 코드 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2) # start, end 파라미터 없이 호출
print(list2)

# 테스트 코드 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3) # start, end 파라미터 없이 호출
print(list3)