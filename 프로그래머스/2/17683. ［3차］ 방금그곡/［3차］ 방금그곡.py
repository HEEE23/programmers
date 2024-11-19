def solution(m, musicinfos):
    answer = ''
    
    m = list(m)
    for i in range(len(m)):
        if m[i] == '#':
            m[i-1] = m[i-1].lower()
            m[i] = '' 
    m = ''.join(m)
    
    lst = []
    for music in musicinfos:
        start, end, title, info = music.split(',')
        start_hour, start_minute = start.split(':')
        end_hour, end_minute = end.split(':')
        minute = (int(end_hour)*60+int(end_minute))-(int(start_hour)*60+int(start_minute))
        
        info = list(info)
        for i in range(len(info)):
            if info[i] == '#':
                info[i-1] = info[i-1].lower()
                info[i] = ''
        info = ''.join(info)
        
        melody = ''
        for i in range(minute):
            melody += info[i%len(info)]
        
        if m in melody:
            lst.append((title, minute))
    
    if not lst:
        return '(None)'
    
    lst.sort(key = lambda x : -x[1])
    answer = lst[0][0]
    return answer