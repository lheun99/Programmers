def solution(quiz):
    answer = []
    for pr in quiz:
        pr = pr.replace("=", "==")

        if eval(pr):
            answer.append("O")
        else:
            answer.append("X")

    return answer
