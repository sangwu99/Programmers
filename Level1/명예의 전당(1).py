def solution(k, score):
    answer = []
    myung = []
    for i in score:
        myung.append(i)
        myung.sort(reverse=True)
        myung = myung[:k]
        answer.append(myung[-1])
    return answer