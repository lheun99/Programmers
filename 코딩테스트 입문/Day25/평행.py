from itertools import combinations as cb


def solution(dots):
    comb = list(cb(dots, 2))

    gradient = []
    for com in comb:
        gra = (com[1][1]-com[0][1])/(com[1][0]-com[0][0])
        if gra in gradient:
            return 1
        gradient.append(gra)

    return 0
