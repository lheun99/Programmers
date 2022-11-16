# 방법1
def solution(s):
    num_p = 0
    num_y = 0

    for i in s.lower():
        if i == "p":
            num_p += 1
        elif i == "y":
            num_y += 1

    return num_p == num_y

# 방법2_count()


def solution(s):
    return s.lower().count("p") == s.lower().count("y")
