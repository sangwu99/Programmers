def solution(food):
    answer = ''
    for i in range(1,len(food)):
        answer += "{}".format(i)*int(food[i]/2)
    answer = answer + "0" + answer[::-1]
    return answer