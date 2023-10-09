import math
from fractions import Fraction


def solution(denum1, num1, denum2, num2):
    num = Fraction(denum1, num1) + Fraction(denum2, num2)
    answer = [num.numerator, num.denominator]

    return answer


def solution2(numer1, denom1, numer2, denom2):
    num1 = denom1 * denom2
    num2 = (numer1 * denom2) + (numer2 * denom1)

    gcd = math.gcd(num1, num2)

    print(num2//gcd, num1//gcd)


solution2(1, 2, 3, 4)
solution2(9, 2, 1, 3)
