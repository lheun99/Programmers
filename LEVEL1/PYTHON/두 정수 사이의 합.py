# 방법1
def solution(a, b):
    if b < a:
        temp = a
        a = b
        b = temp
    data = [i for i in range(a, b+1)]
    return sum(data)

# 방법2


def solution(a, b):
    if b < a:
        a, b = b, a
    data = range(a, b+1)

    return sum(data)
