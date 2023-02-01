def solution(k, score):
    rank = []
    answer = []
    for sc in score:
        rank.append(sc)
        rank.sort(reverse=True)
        answer.append(rank[:k][-1])

    return answer
