def solution(today, terms, privacies):
    answer = []
    termdict = {}
    a=1
    today_years = today.split(".")[0]
    today_month = today.split(".")[1]
    today_date = today.split(".")[2]
    today_sum = int(today_years)*336 + int(today_month)*28 + int(today_date)
    for i in terms:
        termdict[i.split()[0]] = int(i.split()[1])
    for i in privacies:
        term = i.split()[1]
        made_years = i.split()[0].split(".")[0]
        made_month = i.split()[0].split(".")[1]
        made_date = i.split()[0].split(".")[2]
        made_sum = int(made_years)*336 + int(made_month)*28+ int(made_date)
        if (today_sum - made_sum) >= termdict[term]*28:
            answer.append(a)
        a += 1
    return answer