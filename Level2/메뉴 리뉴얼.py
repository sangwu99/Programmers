def solution(orders, course):
    answer = []
    from itertools import combinations
    for i in course:
        guide_dict = {}
        max_item = []
        max_num = 2
        for j in orders:
            for p in combinations(j,i):
                p = "".join(sorted(p))
                if p in guide_dict:
                    guide_dict[p] += 1
                else:
                    guide_dict[p] = 1 
        for k,l in guide_dict.items():
            if l>max_num:
                max_num = l
                max_item = [k]
            elif l==max_num:
                max_item.append(k)
            else:
                pass
        for m in max_item:
            answer.append(m)
                
    return sorted(answer)