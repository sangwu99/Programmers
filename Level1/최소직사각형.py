def solution(sizes):
    garo = 0
    sero = 0
    for i in sizes:
        a, b = max(i),min(i)
        if a > garo:
            garo = a
        if b > sero:
            sero = b 
    return garo*sero