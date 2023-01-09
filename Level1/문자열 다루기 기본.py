def solution(s):
    if ((len(s)==4)|(len(s)==6))&(s.lower()==s.upper()):
        return True
    else:
        return False