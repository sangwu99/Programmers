def solution(p):
    if p=='':
        return ''
    else: 
        a = 0 
        for i in range(len(p)):
            if p[i]=='(':
                a+=1
            else:
                a-=1
            if a ==0:
                break
        u,v = p[:i+1],p[i+1:]
        a = 0 
        for i in range(len(u)):
            if u[i]=='(':
                a+=1
            else:
                a-=1
            if a<0:
                b = '(' + solution(v) + ')' 
                for i in u[1:-1]:
                    if i=='(':
                        b +=')'
                    else:
                        b +='('
                return b 
        else:
             return u + solution(v)   

