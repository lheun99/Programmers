# 방법1
def solution(my_string):
    my_string = my_string.split(" ")
    num = []
    al = []
    for i in my_string:
        if i.isdigit():
            num.append(int(i))
        else:
            al.append(i)

    answer = num.pop(0)
    for op in al:
        if op == '+':
            answer += num.pop(0)
        elif op == '-':
            answer -= num.pop(0)

    return answer

# 방법2


def solution(my_string):
    return eval(my_string)
