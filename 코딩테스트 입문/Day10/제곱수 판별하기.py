# 방법1
import math


def solution(n):
    answer = 1 if math.sqrt(n) % 1 == 0 else 2

    return answer

# 방법2


def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'
