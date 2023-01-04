from math import gcd

def solution(denum1, num1, denum2, num2):
    answer = []
    son = (denum1*num2) + (denum2*num1) 
    mother = num1*num2 
    dev = gcd(son,mother)
    answer.append(son/dev)
    answer.append(mother/dev)
    return answer