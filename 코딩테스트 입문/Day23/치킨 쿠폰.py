def solution(chicken):
    answer = 0
    cnt = chicken//10
    coupon = (chicken % 10) + cnt

    while cnt > 0:
        answer += cnt
        cnt = coupon//10
        coupon = (coupon % 10) + cnt

    return answer
