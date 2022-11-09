def solution(num, total):
    sum_n = sum(range(num, num*2))

    start = (sum_n - total)//num
    answer = list(range(num-start, num*2-start))

    return answer
