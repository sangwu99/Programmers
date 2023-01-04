
def solution(num, total):
    answer = []
    if total !=0:
        dev,ex = divmod(total,num)
        if ex==0:
            for i in range(num):
                j = dev - (num//2) + i
                answer.append(j)
        else:
            for i in range(num):
                j = dev - ((num//2)-1) + i
                answer.append(j)
    else:
        ex = num//2
        for i in range(num):
            j = -ex + i
            answer.append(j)
    return answer