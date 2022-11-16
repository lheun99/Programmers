def solution(num):
    if num == 1:
        return 0

    cnt = 1
    while cnt <= 500:
        if num % 2 == 0:
            num //= 2
        else:
            num = (num*3) + 1

        if num == 1:
            return cnt
        cnt += 1

    return -1
