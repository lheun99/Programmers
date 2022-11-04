def solution(array, n):
    array.sort()
    min_num = 9999
    for num in array:
        if abs(min_num-n) > abs(num-n):
            min_num = num
    return min_num
