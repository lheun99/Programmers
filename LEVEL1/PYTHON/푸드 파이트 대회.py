def solution(food):
    nums = [food[i]//2 for i in range(1, len(food))]

    half = "".join([str(idx+1) * num for idx, num in enumerate(nums)])

    answer = half + "0" + half[::-1]

    return answer
