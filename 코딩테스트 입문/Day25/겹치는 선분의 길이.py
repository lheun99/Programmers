def solution(lines):
    lines = [set(range(nums[0], nums[1])) for nums in lines]

    overlap = []
    for i in range(0, 3):
        overlap.append(lines[i] & lines[(i+1) % 3])

    answer = list(overlap[0] | overlap[1] | overlap[2])

    return len(answer)
