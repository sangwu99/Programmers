from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for p in permutations(dungeons,len(dungeons)):
        health = k
        adventure = 0
        for j in p:
            if j[0] <= health:
                adventure += 1
                health -= j[1]
        if adventure > answer:
            answer = adventure
        if answer == len(dungeons):
            break   
    return answer