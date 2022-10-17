def solution(my_string, n):
    answer = ''
    for alphabet in my_string:
        answer += alphabet * n
    return answer
