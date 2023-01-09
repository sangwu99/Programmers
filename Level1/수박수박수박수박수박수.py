def solution(n):
    answer = ""
    for i in range(0,n+1,2):
        answer += '수'
        answer += '박'
    
    return answer[:n]