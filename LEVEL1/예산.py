def solution(d, budget):
    answer = []
    d.sort()

    for num in d:
        budget -= num
        if budget < 0:
            break
        print(num)
        answer.append(num)

    return len(answer)

# 시간 초과
# from itertools import combinations as cb


# def solution(d, budget):
#     teams_list = []
#     for i in range(1, len(d) + 1):
#         teams_list += cb(d, i)

#     can_list = []
#     for teams in teams_list:
#         if sum(teams) <= budget:
#             can_list.append(len(teams))

#     return max(can_list)
