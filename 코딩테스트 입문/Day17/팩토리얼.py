def fact(n):
    if n == 1:
        return 1
    else:
        return n*(fact(n-1))


def solution(n):
    answer = 0
    num = 0
    while num <= n:
        answer += 1
        num = fact(answer)

    return answer-1
