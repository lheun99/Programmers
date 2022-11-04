def solution(my_string):
    answer = 0
    word = ""

    for al in my_string:
        if al.isdigit():
            word += str(al)
        elif len(word) > 0:
            answer += int(word)
            word = ""
        else:
            continue

    if len(word) > 0:
        answer += int(word)

    if answer == 0:
        return 0
    return answer
