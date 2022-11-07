from collections import deque


def solution(A, B):
    A = deque(A)

    for i in range(0, len(B)):
        if list(A) == list(B):
            return i
        A.rotate(1)
    return -1
