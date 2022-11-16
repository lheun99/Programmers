def solution(absolutes, signs):
    data = []
    for pair in zip(absolutes, signs):
        if not pair[1]:
            data.append(pair[0]*-1)
        else:
            data.append(pair[0])
    return sum(data)
