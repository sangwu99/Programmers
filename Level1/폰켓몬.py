def solution(nums):
    sets = set(nums)
    if len(sets) <= len(nums)/2:
        answer = len(sets)
    else:
        while len(sets) > len(nums)/2:
            sets.pop()
        answer = len(sets)
    return answer