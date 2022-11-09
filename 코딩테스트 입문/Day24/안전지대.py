def solution(board):
    length = len(board)
    idx_arr = []
    dx = [-1, 0, 1]
    dy = [-1, 0, 1]
    for r, part in enumerate(board):
        for c, num in enumerate(part):
            if num == 1:
                for x in dx:
                    for y in dy:
                        idx_arr.append((r+x, c+y))

    answer = 0
    idx_arr = set(idx_arr)

    for x, y in idx_arr:
        if 0 <= x < length and 0 <= y < length:
            answer += 1

    return (length**2) - answer
