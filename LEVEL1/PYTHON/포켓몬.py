def solution(nums):
    origin_nums = nums.copy()
    nums = list(set(nums))

    if len(nums) > len(origin_nums)//2:
        return len(origin_nums)//2
    return len(nums)
