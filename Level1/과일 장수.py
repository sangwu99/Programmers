def solution(k, m, score):
    answer=0
    score.sort(reverse=True)
    le=len(score)//m
    for i in range(le):
        try:
            new_list = score[i*m:(i+1)*m]
            answer +=min(new_list)*m
        except:
            pass
    return answer