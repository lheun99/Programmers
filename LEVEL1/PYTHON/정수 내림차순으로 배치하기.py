def solution(n):
    nums = [i for i in str(n)]
    nums.sort(reverse=True)

    return int("".join(nums))
