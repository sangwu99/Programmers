def solution(n):
    a = n+1
    s = bin(n)
    while s.count("1") != bin(a).count("1") :
        a += 1
    return a