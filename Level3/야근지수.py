import heapq

def solution(n, works):
    answer = 0
    heap = []
    for i in works:
        heapq.heappush(heap,-i)
    for _ in range(n):
        heapq.heappush(heap,(heapq.heappop(heap) + 1))
    for i in heap:
        if i>=0:
            pass
        else:
            answer += i**2
        
    return answer