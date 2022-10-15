def solution(n):
    nums = [i for i in range(1, n+1)]
    answer = list(filter(lambda x: x % 2 != 0, nums))
    return answer
