def solution(N, stages):
    num_list = {}
    answer = []
    for i in range(1,N+1):
        do = 0
        jung = 0
        for j in stages:
            if j>i:
                do += 1 
            elif j==i:
                do += 1
                jung += 1
        if do==0:
            num_list[i]= (0)
        else:
            num_list[i]= (jung/do)
    answers = sorted(num_list.items(), key=lambda item : item[1],reverse=True)
    for i in answers:
        answer.append(i[0])
    return answer

