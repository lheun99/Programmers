# 방법1
from itertools import combinations as cb


def solution(numbers):
    if len(numbers) == 2:
        return numbers[0]*numbers[1]

    nums = cb(numbers, 2)
    max_n = 0
    for x, y in nums:
        if x*y > max_n:
            max_n = x*y
    return max_n

# 방법2


def solution(numbers):
    numbers.sort()
    return max(numbers[0]*numbers[1], numbers[-1]*numbers[-2])
