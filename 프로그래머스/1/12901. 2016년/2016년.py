def solution(a, b):
    import datetime
    answer = ''
    day = datetime.datetime(2016, a, b).weekday()
    
    if day == 0: answer = 'MON'
    elif day == 1: answer = 'TUE'
    elif day == 2: answer = 'WED'
    elif day == 3: answer = 'THU'
    elif day == 4: answer = 'FRI'
    elif day == 5: answer = 'SAT'
    else: answer = 'SUN'
    return answer