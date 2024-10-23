from math import ceil
def solution(fees, records):
    answer = []
    
    # 기본 시간, 기본 요금, 단위 시간, 단위 요금
    default_time, default_fee, unit_time, unit_fee = fees
    
    # 누적 주차시간 
    cumulation = {}
    # 주차시간
    parking = {}
    for r in records:
        time, num, state = r.split()
        h, m = map(int,time.split(":"))

        time = h*60 + m
        if state == 'IN':
            parking[num] = time
        elif state == 'OUT':
            if num in cumulation:
                cumulation[num] += (time - parking[num])
            else:
                cumulation[num] = (time - parking[num])
            del parking[num]
    
    # 출차된 내역이 없으면, 23:59에 출차
    for num, time in parking.items():
        if num in cumulation:
            cumulation[num] += (1439-time)
        else:
            cumulation[num] = (1439-time)
            
    for num, time in sorted(cumulation.items(), key = lambda x : x[0]):
        answer.append(default_fee+ max(0,ceil((time-default_time)/unit_time)) * unit_fee)
    return answer