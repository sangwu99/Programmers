def solution(s):
    answer_list = []
    for i in range(len(s.split())):
        answer_list.append(int(s.split()[i]))
    return "{} {}".format(min(answer_list),max(answer_list))