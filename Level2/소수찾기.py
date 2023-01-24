def solution(numbers):
    answer = 0
    numbers = list(numbers)
    used = []
    used.append(0)
    used.append(1)
    from itertools import permutations
    for j in range(1,len(numbers)+1):
        for p in permutations(numbers,j):
            guide_str = ""
            for k in p:
                guide_str+=k
            guide_str = int(guide_str)
            if guide_str in used:
                pass
            else:
                for i in range(2,int(guide_str**0.5)+1):
                    if (guide_str%i)==0:
                        break
                else:
                    answer+=1
            used.append(guide_str)
    return answer