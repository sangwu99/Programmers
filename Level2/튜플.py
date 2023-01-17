def solution(s):
    answer_dict = {}
    answer = []
    s = s.split(",{")
    for i in s:
        i = i.replace("{","")
        i = i.replace("}","")
        i = i.split(",")
        answer_dict[len(i)] = i
    for j in range(1,len(answer_dict)+1):
        for k in answer_dict[j]:
            if int(k) not in answer:
                answer.append(int(k))
    return answer