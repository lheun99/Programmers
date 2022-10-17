# 방법 1
def solution(numbers):
    answer = sum(numbers)/len(numbers)
    return answer

# 방법 2 statistics
#from statistics import mean


def solution(numbers):
    answer = mean(numbers)
    return answer


# 방법 3 numpy
#import numpy as np
def solution(numbers):
    answer = np.mean(numbers)
    return answer
