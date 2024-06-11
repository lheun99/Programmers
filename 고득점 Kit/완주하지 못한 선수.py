def solution(participant, completion):
    answer = ''

    dict_1 = {}
    for p in participant:
        if p not in dict_1:
            dict_1[p] = 1
        else: 
            dict_1[p] += 1
    
    for c in completion:
        if c in dict_1.keys():
            dict_1[c] -= 1

    for k, v in dict_1.items():
        if v != 0:
            answer += k

    return answer

print(solution(["mislav", "stanko", "mislav", "ana"], 	["stanko", "ana", "mislav"]))