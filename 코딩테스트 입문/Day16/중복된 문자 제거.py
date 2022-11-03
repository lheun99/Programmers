from collections import Counter


def solution(my_string):
    my_string = Counter(my_string)

    answer = "".join(list(my_string.keys()))
    return answer
