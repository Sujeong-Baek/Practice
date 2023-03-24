# 합병 정렬 알고리즘 중 사용되는 merge 함수를 작성해 보세요.
# merge 함수는 정렬된 두 리스트 list1과 list2를 받아서, 하나의 정렬된 리스트를 리턴합니다.

def merge(list1, list2):
    # 여기에 코드를 작성하세요
    mergelist=[]
    while list1 and list2:
        if list1[0] < list2[0]:
            mergelist.append(list1[0])
            list1.remove(list1[0])
        else:
            mergelist.append(list2[0])
            list2.remove(list2[0])
    if list1:
        mergelist.extend(list1) 
    else:
        mergelist.extend(list2)
    return mergelist



    
    
    

# 테스트 코드
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))