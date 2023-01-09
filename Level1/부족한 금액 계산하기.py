def solution(price, money, count):
    total = 0 
    if count!=1:
        for i in range(1,count+1):
            total += price*i
    else:
        total = price
    if (total - money) <0:
        answer = 0
    else:
        answer = total - money 
    return answer