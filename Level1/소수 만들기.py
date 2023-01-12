def solution(nums):
    answer = 0
    from itertools import combinations
    for p in combinations(nums,3):
        t = True
        for j in range(2,sum(p)):
            if sum(p)%j==0:
                t = False
        if t == True:
            answer += 1
    return answer