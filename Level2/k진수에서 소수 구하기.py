def solution(n, k):
    answer = 0
    jinsu = ""
    while n:
        n, i = divmod(n,k)
        jinsu += str(i)
    jinsu = jinsu[::-1].split("0")
    for j in jinsu:
        if (j=='1')|(j==""):
            continue
        j = int(j)
        for k in range(2,int(j**0.5)+1):
            if j%k==0:
              break
        else:
            answer+=1  
    return answer