# 방법1
def solution(cipher, code):
    answer = ''
    for idx in range(code, len(cipher)+1, code):
        answer += cipher[idx-1]
    return answer
# 방법2


def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer
