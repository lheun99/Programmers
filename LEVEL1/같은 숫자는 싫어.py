# 방법1
def solution(arr):
    stack = []
    stack.append(arr[0])
    for num in arr:
        if num != stack[-1]:
            stack.append(num)

    return stack

# 방법2


def solution(arr):
    stack = []
    for num in arr:
        if [num] != stack[-1:]:
            stack.append(num)
    return stack
