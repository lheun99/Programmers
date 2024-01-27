def getDivisor(n):
    _list = []
    for i in range(1, int(n**(1/2))+1):
        if(n%i) == 0:
            _list.append(i)
            if (i**2) != n:
                _list.append(n//i)
    return len(_list)

def solution(number, limit, power):
    armor = []
    for i in range(1, number + 1):
        armor.append(getDivisor(i))   
    
    for idx, a in enumerate(armor):
        if a > limit:
            armor[idx] = power

    return sum(armor)