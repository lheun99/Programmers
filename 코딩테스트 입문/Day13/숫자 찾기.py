def solution(num, k):
    num = str(num)
    answer = num.find(str(k))

    if answer == -1:
        return -1
    return answer + 1
