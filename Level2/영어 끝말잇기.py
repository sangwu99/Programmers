def solution(n, words):
    dup = []
    Cap= words[0][0]
    num=0
    turn = 0
    for i in range(len(words)):
        if (words[i] in dup) | (words[i][0]!=Cap):
            num = (i)%n +1
            turn = (i//n) +1
            break
        else:
            Cap = words[i][-1] 
            dup.append(words[i])
    answer = [num,turn]
    return answer