def solution(dots):
    dots.sort()
    w = dots[2][0] - dots[1][0]
    h = dots[3][1] - dots[2][1]
    return w*h
