def solution(elements):
    answer = 0
    new_list = []
    for i in range(1,len(elements)+1):
        for j in range(len(elements)):
            new_list.append(sum((elements*2)[j:j+i]))
    answer = len(set(new_list))
    return answer