def solution(s):
    dic = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
           "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    answer = s
    for eng in dic.keys():
        if eng in s:
            answer = answer.replace(eng, str(dic[eng]))

    return int(answer)
