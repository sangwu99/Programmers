def solution(a, b, n):
    answer = 0
    c = 1
    while c > 0:
        c, d = divmod(n,a)
        answer += (c*b)
        n = (c*b)+d
    return answer