def solution(emergency):
    answer = [0]*len(emergency)
    order = sorted(emergency, reverse=True)

    for idx, num in enumerate(order):
        answer[emergency.index(num)] = idx+1

    return answer
