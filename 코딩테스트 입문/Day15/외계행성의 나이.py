def solution(age):
    a = ord('a')
    answer = ''
    for i in str(age):
        answer += chr(a+int(i))
    return answer
