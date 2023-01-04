def solution(quiz):
    answer = []
    for i in quiz:
        a,b,c,d,e = i.split(" ")
        a,c,e = int(a), int(c), int(e)
        if b == "+":
            if e == a+c:
                answer.append("O")
            else:
                answer.append("X")
        else:
            if e == a-c:
                answer.append("O")
            else:
                answer.append("X")
    return answer