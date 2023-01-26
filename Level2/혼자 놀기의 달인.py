from collections import Counter

def find(parent,x):
    if parent[x] !=x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b 
    
def solution(cards):
    parent = [i for i in range(len(cards)+1)]
    for i,k in enumerate(cards):
        union(parent,i+1,k)
    
    for i in range(len(parent)):
        parent[i] = find(parent,i)
        
    if Counter(parent).most_common(2)[1][0]==0:
        answer = 0
    else:
        answer = int(Counter(parent).most_common(2)[0][1]) * int(Counter(parent).most_common(2)[1][1])
    return answer