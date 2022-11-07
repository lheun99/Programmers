def solution(s):
    s = s.split(" ")
    answer = []
    for w in s:
        if w == 'Z':
            answer.pop()
        else:
            answer.append(int(w))
    return sum(answer)
