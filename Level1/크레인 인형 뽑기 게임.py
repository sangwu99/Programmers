def solution(board, moves):
    answer = 0
    answer_list = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]==0:
                pass
            else:
                answer_list.append(board[j][i-1])
                board[j][i-1] = 0
                break
        try:
            if answer_list[-1] == answer_list[-2]:
                answer_list.pop()
                answer_list.pop()
                answer+=2
            else:
                pass
        except:
            pass
    return answer