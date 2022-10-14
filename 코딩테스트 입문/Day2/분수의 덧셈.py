from fractions import Fraction


def solution(denum1, num1, denum2, num2):
    num = Fraction(denum1, num1) + Fraction(denum2, num2)
    answer = [num.numerator, num.denominator]

    return answer
