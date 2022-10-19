def solution(n):
    nums = list(filter(lambda x: x % 2 == 0, range(n+1)))
    return sum(nums)
