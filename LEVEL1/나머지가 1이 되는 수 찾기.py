def solution(n):
    div = 1
    while True:
        if n % div == 1:
            return div
        div += 1
