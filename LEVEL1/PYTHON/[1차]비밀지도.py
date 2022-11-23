def solution(n, arr1, arr2):
    map = []
    for n1, n2 in zip(arr1, arr2):
        map.append((bin(n1 | n2)[2:]).zfill(n))

    answer = []
    for line in map:
        line = line.replace("1", "#")
        line = line.replace("0", " ")
        answer.append(line)
    return answer