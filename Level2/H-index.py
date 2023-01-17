def solution(citations):
    answer = [0]
    for i in range(1,len(citations)+1):
        ans = 0
        for j in citations:
            if j >= i:
                ans +=1
        if ans >= i:
            answer.append(i)
    return max(answer)