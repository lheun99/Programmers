from collections import Counter


def solution(s):
    cnt_list = Counter(s)
    answer = ''
    for al, cnt in cnt_list.items():
        if cnt == 1:
            answer += al

    return "".join(sorted(answer))
