# 방법 1
from string import ascii_lowercase, ascii_uppercase


def solution(s, n):
    answer = ""
    upper_al = list(ascii_uppercase)
    lower_al = list(ascii_lowercase)

    for al in s:
        if al in upper_al:
            answer += upper_al[(upper_al.index(al) + n) % 26]

        elif al in lower_al:
            answer += lower_al[(lower_al.index(al) + n) % 26]

        else:
            answer += al

    return answer

# 방법 2


def solution(s, n):
    answer = ""

    for al in s:
        if al.isupper():
            answer += chr(((ord(al)-ord('A')+n) % 26) + ord("A"))

        elif al.islower():
            answer += chr(((ord(al)-ord('a')+n) % 26) + ord("a"))

        else:
            answer += al

    return answer
