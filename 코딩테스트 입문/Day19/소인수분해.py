def solution(n):
    one = []
    for num in range(2, n+1):
        if n % num == 0:
            one.append(num)

    answer = []
    for num in one:
        cnt = 0
        for n in range(2, num+1):
            if num % n == 0:
                cnt += 1
        if cnt == 1:
            answer.append(num)
    return answer
