def solution(sizes):
    w_list = []
    h_list = []

    for i, j in sizes:
        w_list.append(max(i, j))
        h_list.append(min(i, j))

    return max(w_list)*max(h_list)
