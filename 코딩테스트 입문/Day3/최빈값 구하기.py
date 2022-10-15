from collections import Counter


def solution(array):
    cnt = Counter(array).most_common()
    _most = cnt[0]

    if len(cnt) == 1:
        return _most[0]

    _next = cnt[1]

    if _most[1] == _next[1]:
        return -1

    return _most[0]
