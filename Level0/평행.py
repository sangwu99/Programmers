def solution(dots):
    answer = 0
    for i in dots:
        for j in dots:
            for k in dots:
                for l in dots:
                    if i==j:
                        pass
                    elif k==l:
                        pass
                    elif i==k:
                        pass
                    elif i==l:
                        pass
                    elif j==k:
                        pass
                    elif j==l:
                        pass
                    elif (i[1] - j[1])/(i[0]-j[0]) == (k[1] - l[1])/(k[0]-l[0]): 
                        answer=1
                    else:
                        pass
                
    return answer