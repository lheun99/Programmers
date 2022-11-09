def solution(polynomial):
    polynomial = polynomial.split(" + ")
    x_num = 0
    num = 0
    for word in polynomial:
        if "x" in word:
            if word == "x":
                x_num += 1
            else:
                word = word.replace("x", "")
                x_num += int(word)
        else:
            num += int(word)

    answer = ""

    if x_num == 0:
        return str(num)
    elif x_num == 1:
        answer += "x"
    else:
        answer += str(x_num) + "x"

    if num == 0:
        return answer
    return f"{answer} + {str(num)}"
