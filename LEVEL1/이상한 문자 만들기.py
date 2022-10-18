def solution(s):
    answer = []
    for word in s.split(" "):
        change = [alphabet.upper() if idx % 2 == 0 else alphabet.lower() for idx,
                  alphabet in enumerate(word)]
        answer.append("".join(change))

    return " ".join(answer)
