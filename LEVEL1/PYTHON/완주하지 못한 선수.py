def solution(participant, completion):
    participant.sort()
    completion.sort()

    for one, two in zip(participant, completion):
        if one != two:
            return one
    return participant[-1]
