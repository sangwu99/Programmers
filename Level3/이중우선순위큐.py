import heapq

def solution(operations):
    usun = []
    for i in operations:
        i = i.split(' ')
        try:
            if i[0]=='I':
                heapq.heappush(usun,int(i[1]))
            elif (i[0]=='D')and (i[1]=='1'):
                usun.pop(-1)
            else:
                heapq.heappop(usun)
        except:
            pass
    if len(usun)==0:
        answer = [0,0]
    else:
        answer = [max(usun),min(usun)]
    return answer