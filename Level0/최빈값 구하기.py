from collections import Counter
def solution(array):
    answer = 0
    max_count = 0
    modes = []
    for c in set(array):
        if max_count <= Counter(array)[c]:
            max_count = Counter(array)[c]
            nodes = c 
            modes.append(max_count)
    if Counter(modes)[max(modes)] != 1:
        answer = -1
    else:
        answer = nodes
    return answer