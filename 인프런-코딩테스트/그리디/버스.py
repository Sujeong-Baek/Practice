def solution(limit, weight):
    weight.sort()
    answer=0
    total=0
    for w in weight:
        if total+w>limit:
            return answer
        total+=w
        answer+=1


limit=700
weight=[300,100,230,120,90,150,60]
print(solution(limit, weight))