from itertools import combinations as cb


def solution(nums):
    nums_list = list(cb(nums, 3))
    num_list = [sum(numbers) for numbers in nums_list]
    num_list.sort()

    answer = 0

    for num in num_list:
        cnt = 0
        for i in range(2, int(num**(0.5))+1):
            if num % i == 0:
                cnt += 1
        if cnt == 0:
            answer += 1

    return answer
