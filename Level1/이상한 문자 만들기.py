def solution(s):
    answer_list = []
    s = s.split(" ")
    for j in range(len(s)):
        answer = ""
        for i in range(len(s[j])):
            if (i==0)|((i%2)==0):
                answer += s[j][i].upper()
            else:
                answer += s[j][i].lower()
        answer_list.append(answer)
    return " ".join(answer_list)