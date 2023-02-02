a,b = map(int,input().split())

cnt = 0
while a!=b:
    if b-a >= 8:
        a += 10
    elif b-a >= 3:
        a += 5
    elif b-a >= 0:
        a +=1
    elif b-a >= -3:
        a -=1
    elif b-a >=-8:
        a -=5
    else:
        a -=10
    cnt +=1

print(cnt)