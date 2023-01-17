def solution(arr):
    finish = True
    arr.sort()
    i = 1
    while finish:
        lcm = arr[-1] * i
        for j in arr[:-1]:
            if (lcm%j)!=0:
                i += 1
                break
        else:
            finish = False
    return lcm