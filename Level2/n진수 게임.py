def make_jinsu(n, num):
    base_eng = "ABCDEF"
    num_dict = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    ans = ""
    while num:
        num, a = divmod(num,n)
        if a >= 10:
            ans+= num_dict[a]
        else:
            ans+= str(a)
    if ans =="":
        ans = "0"
    return ans[::-1]
        
def solution(n, t, m, p):
    answer = ''
    full_ans = ""
    for i in range(0,t*m):
        full_ans += make_jinsu(n,i)
    for j in range(t):
        answer += full_ans[j*m+p-1]
    return answer