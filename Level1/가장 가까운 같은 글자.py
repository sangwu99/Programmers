def solution(s):
    answer = []
    script = ""
    for i in range(len(s)):
        if s[i] in script:
            answer.append(i-script.rfind(s[i]))
            script += s[i]
        else:
            answer.append(-1)
            script += s[i]
    return answer