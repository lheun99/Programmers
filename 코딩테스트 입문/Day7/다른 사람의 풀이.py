# 방법1
def solution(array, n):
    answer = [i for i in array if n == i]
    return len(answer)
# 방법2


def solution(array, n):
    return array.count(n)
