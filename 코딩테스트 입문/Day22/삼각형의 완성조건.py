def solution(sides):
    num_1 = max(sides) - min(sides)
    list_1 = list(range(num_1+1, max(sides)+1))

    num_2 = sum(sides)
    list_2 = list(range(max(sides)+1, num_2))

    return len(list_1 + list_2)
