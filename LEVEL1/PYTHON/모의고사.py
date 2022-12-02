def solution(answers):
    first = [1, 2, 3, 4, 5]
    f_len = len(first)
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    s_len = len(second)
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    t_len = len(third)

    result = [0]*3
    one, two, three = 0, 0, 0
    for idx, num in enumerate(answers):
        if num == first[idx % f_len]:
            result[0] += 1
        if num == second[idx % s_len]:
            result[1] += 1
        if num == third[idx % t_len]:
            result[2] += 1

    max_n = max(result)
    answer = []
    for idx, num in enumerate(result):
        if num == max_n:
            answer.append(idx+1)
    return answer
