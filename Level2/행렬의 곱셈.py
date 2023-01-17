def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        row_list = []
        for k in range(len(arr2[0])):
            val = 0
            for j in range(len(arr1[0])):
                val += arr1[i][j] * arr2[j][k]
            row_list.append(val)
        answer.append(row_list)
    return answer