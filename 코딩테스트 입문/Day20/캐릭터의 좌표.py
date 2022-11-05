def solution(keyinput, board):
    rule = {"up": [0, 1], "down": [0, -1], "left": [-1, 0], "right": [1, 0]}

    limit_w = board[0]//2
    limit_h = board[1]//2

    answer = [0, 0]
    temp = [0, 0]

    for key in keyinput:
        temp[0] += rule[key][0]
        temp[1] += rule[key][1]

        if abs(temp[0]) <= limit_w and abs(temp[1]) <= limit_h:
            answer[0] = temp[0]
            answer[1] = temp[1]

        else:
            temp[0] -= rule[key][0]
            temp[1] -= rule[key][1]

    return answer
