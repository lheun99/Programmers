def solution(n, t):
    virus = n
    for time in range(1, t+1):
        virus = virus * 2
    return virus
