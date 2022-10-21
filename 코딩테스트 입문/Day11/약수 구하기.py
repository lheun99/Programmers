def solution(n):
    nums = [num for num in range(1, n+1)]
    answer = list(filter(lambda x: n % x == 0, nums))
    return answer
