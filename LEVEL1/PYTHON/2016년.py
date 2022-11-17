def solution(a, b):
    month_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    jan_day = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    day = ["SAT","SUN","MON","TUE","WED","THU","FRI"]
    days = 0
    
    if a == 1:
        return jan_day[b-1]
    
    else:
        days = 30
        for month in range(2, a+1):
            if month == a:
                days += b
            else:
                days += month_day[month]
            
        return day[(days%7)-1]