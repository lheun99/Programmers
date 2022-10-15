# 방법1_statistics.median(arr)
from statistics import median


def solution(array):
    return median(array)


# 방법2
def solution(array):
    array.sort()
    return array[len(array)//2]
