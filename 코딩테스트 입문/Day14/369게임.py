def solution(order):
    tsn = ['3', '6', '9']
    cnt = 0
    for i in str(order):
        if i in tsn:
            cnt += 1
    return cnt
