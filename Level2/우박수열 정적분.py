def solution(k, ranges):
    answer = []
    a=0
    guide = [(a,k)]
    while k!=1:
        if (k%2)==0:
            k= (k/2)
        else:
            k = (k*3) +1
        a +=1
        guide.append((a,k))
    neorb = []
    for i in range(0,len(guide)-1):
        minimum,maximum  = min(guide[i][1],guide[i+1][1]), max(guide[i][1],guide[i+1][1])
        neorb.append(minimum+((maximum-minimum)*0.5))
    for i in ranges:
        if i[0] > (len(guide)-1+i[1]):
            answer.append(-1)
        elif i[0] == (len(guide)-1+i[1]):
            answer.append(0)
        else:
            if i[1]==0:
                answer.append(sum(neorb[i[0]:]))
            else:
                answer.append(sum(neorb[i[0]:i[1]]))
    return answer