def solution(t, p):
    nums = [int(t[i:i+len(p)]) for i in range(len(t)-len(p)+1)]
    
    answer = [num for num in nums if num <= int(p)]
    return len(answer)