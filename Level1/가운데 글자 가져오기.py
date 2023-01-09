def solution(s):
    if len(s)%2==0:
        answer = s[1:3]
        answer = s[int(((len(s)/2)-1)):int(((len(s)/2)+1))]
    else:
        answer = s[len(s)//2]
    return answer