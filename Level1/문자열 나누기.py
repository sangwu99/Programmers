def solution(s):
    cnt=0
    while s!="":
        x=s[0]
        a = 0
        b = 0
        for i in range(len(s)):
            if (a==0)|(a!=b):
                if x==s[i]:
                    a +=1
                else:
                    b +=1
            else:
                break
        s = s[a+b:]
        cnt += 1
            
    return cnt