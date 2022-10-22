def solution(n):
    num_list = [num for num in range(1, n+1) if n % num == 0]
    return len(num_list)
