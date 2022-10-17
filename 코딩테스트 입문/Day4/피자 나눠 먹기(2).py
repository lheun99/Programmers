def solution(n):
    for num in range(max(n, 6), (n*6)+1):
        if num % n == 0 and num % 6 == 0:
            return num//6
