def solution(new_id):
    use = "abcdefghijklmnopqrstuvwxyz1234567890-_."
    new_id = new_id.lower()
    need_exctract_list = []
    for i in new_id:
        if i not in use:
            need_exctract_list.append(i)
    for i in need_exctract_list:
        new_id = new_id.replace(i,"")
    for i in range(1000,1,-1):
        new_id = new_id.replace("."*i,"."*(i-1))
    try:
        if new_id[0]==".":
            new_id = new_id[1:]
    except:
        pass
    try:
        if new_id[-1]==".":
            new_id = new_id[:-1]
    except:
        pass
    if new_id =="":
        new_id = "a"
    if len(new_id) >=16:
        new_id = new_id[:15]
    try:
        if new_id[-1]==".":
            new_id = new_id[:-1]
    except:
        pass
    while len(new_id)<3:
        new_id += new_id[-1]
    return new_id