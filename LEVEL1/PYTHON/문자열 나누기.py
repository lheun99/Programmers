def solution(s):
    answer = 0
    x = s[0]
    isX = 0
    notX = 0

    for al in s:
        if isX == notX:
            answer += 1
            x = al

        if al == x:
            isX += 1
        else:
            notX += 1

    return answer
