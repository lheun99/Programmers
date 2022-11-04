def solution(numbers):
    nums = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
            "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    answer = numbers
    for eng, num in nums.items():
        if eng in numbers:
            answer = answer.replace(eng, num)

    return int(answer)
