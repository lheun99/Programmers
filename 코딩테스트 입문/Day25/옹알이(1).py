from itertools import permutations as pm


def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    can_say = []
    for i in range(2, 5):
        can_say += list(pm(can, i))
    says = []
    for say in can_say:
        says.append("".join(list(say)))
    says += can

    cnt = 0
    for bab in babbling:
        if bab in says:
            cnt += 1
    return cnt
