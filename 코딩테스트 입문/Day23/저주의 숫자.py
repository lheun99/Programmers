def solution(n):
    cnt = 1
    num = 1
    nums = []
    while cnt <= n:
        if num % 3 != 0 and "3" not in str(num):
            nums.append(num)
            cnt += 1
        num += 1

    return nums[-1]
