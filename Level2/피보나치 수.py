def solution(n):
    a= 0
    b= 1
    for i in range(n-1):
        a, b = b, a + b
    answer = b % 1234567
    return answer