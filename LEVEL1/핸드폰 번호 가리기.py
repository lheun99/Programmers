def solution(phone_number):
    star = phone_number[0:-4]
    answer = phone_number.replace(star, "*"*len(star))
    return answer
