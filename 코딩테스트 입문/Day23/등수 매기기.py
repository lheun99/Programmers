
def solution(score):
    avg = list(map(lambda x: sum(x)/len(x), score))
    rank = sorted(avg, reverse=True)

    answer = {}
    for idx, s in enumerate(rank):
        if s not in answer:
            answer[s] = idx+1

    return [answer[s] for s in avg]
