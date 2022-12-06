def solution(n, lost, reserve):
    answer = list(range(1, n+1))
    lost.sort()
    
    inter = list(set(lost).intersection(set(reserve)))
    if len(inter) != 0:
        for i in inter:
                reserve.remove(i)
                lost.remove(i)
    
    for l in lost:
        if l-1 in reserve:
            reserve.remove(l-1)
        elif l+1 in reserve:
            reserve.remove(l+1)
        else:
            answer.remove(l)
            
    return len(answer)