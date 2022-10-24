def solution(rsp):
    # 가위는 2 바위는 0 보는 5
    win = ['2', '0', '5']
    answer = ''
    for i in rsp:
        idx = win.index(i)
        answer += win[(idx+1) % 3]
    return answer
