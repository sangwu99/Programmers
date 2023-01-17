def solution(n):
    ans = 1
    while (n//2)>0:
        n,exp = n//2, n%2
        if exp==1:
            ans+=1
    return ans