# 방법1
def solution(n, m):
    answer = []

    # gcd
    for num in range(min(n, m), 0, -1):
        if n % num == 0 and m % num == 0:
            answer.append(num)
            break
    # lcm
    for num in range(max(n, m), n*m+1):
        if num % n == 0 and num % m == 0:
            answer.append(num)
            break

    return answer


# 방법2
#import math

def solution(n, m):
    su1 = math.gcd(n, m)
    su2 = n * m // su1
    return su1, su2
