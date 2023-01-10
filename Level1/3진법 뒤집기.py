def solution(n):
    third_list = []
    while n > 0:
        n, x = divmod(n,3)
        third_list.append(x)
    third = 0    
    for i in range(len(third_list)):
        third += (third_list[i])*(10**i)
    reverse = str(third)[::-1]
    answer = 0
    for i in range(len(reverse)):
        answer += int(reverse[-(i+1)]) * (3**i)        
    return answer