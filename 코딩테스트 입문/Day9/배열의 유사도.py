def solution(s1, s2):
    answer = list(set(s1).intersection(s2))
    return len(answer)
