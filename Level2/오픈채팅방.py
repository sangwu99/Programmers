def solution(record):
    user_dict = {}
    answer = []
    do = []
    for i in record:
        i = i.split(" ")
        if len(i) == 3:
            do.append((i[1],i[0]))
            user_dict[i[1]] = i[2]
        else:
            do.append((i[1],i[0]))
    for j in do:
        if j[1] =="Enter":
            answer.append(user_dict[j[0]]+"님이 들어왔습니다.")
        elif j[1] == "Leave":
            answer.append(user_dict[j[0]]+"님이 나갔습니다.")
        else:
            pass
    return answer