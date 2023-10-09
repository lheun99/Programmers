def solution(name, yearning, photo):
    dict = {}

    for n, y in zip(name, yearning):
        dict[n] = y

    answer = []
    for p in photo:
        s = 0
        for i in p:
            s += dict.get(i, 0)
        answer.append(s)
    return answer


print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], ([
      ["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])))
