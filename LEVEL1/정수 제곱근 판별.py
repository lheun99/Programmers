from math import sqrt


def solution(n):
    if sqrt(n).is_integer():
        return (sqrt(n)+1)**2

    return -1
