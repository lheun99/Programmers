def solution(my_string):
    answer = ''
    for al in my_string:
        if al.isupper():
            answer += al.lower()
        elif al.islower():
            answer += al.upper()
    return answer
