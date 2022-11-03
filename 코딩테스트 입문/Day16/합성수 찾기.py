def solution(n):
    answer = 0
    for num in range(2, n+1):
        cnt = 0
        for i in range(2, num+1):
            if num % i == 0:
                cnt += 1
        if cnt >= 2:
            answer += 1

    return answer
