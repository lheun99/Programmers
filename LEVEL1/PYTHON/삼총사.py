from itertools import combinations as cb


def solution(number):
    pairs = cb(number, 3)
    cnt = 0
    for pair in pairs:
        if sum(pair) == 0:
            cnt += 1
    return cnt
