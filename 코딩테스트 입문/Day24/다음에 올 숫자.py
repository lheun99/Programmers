def solution(common):
    minus_1 = common[1] - common[0]
    minus_2 = common[2] - common[1]
    
    if minus_1 == minus_2:
        return common[-1]+minus_1
    return common[-1]*(common[1]//common[0])
