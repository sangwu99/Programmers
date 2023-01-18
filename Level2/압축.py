def solution(msg):
    base_eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    eng_dict = {}
    answer = []
    a = 27
    for i in range(0,26):
        eng_dict[base_eng[i]] = i+1
    while msg:
        if msg in eng_dict:
            answer.append(eng_dict[msg])
            break
        for i in range(1,len(msg)):
            if msg[:-i] in eng_dict:
                answer.append(eng_dict[msg[:-i]])
                eng_dict[msg[:-i+1]] = a
                a+=1
                msg = msg[len(msg)-i:]
                break
    return answer