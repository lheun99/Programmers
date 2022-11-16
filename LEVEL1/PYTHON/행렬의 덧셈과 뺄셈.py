def solution(arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        temp = []
        for x, y in zip(i, j):
            temp.append(x+y)
        answer.append(temp)
    return answer
