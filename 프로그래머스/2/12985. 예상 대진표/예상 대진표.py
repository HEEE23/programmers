def solution(n,a,b):
    answer = 0

    # 토너먼트 참가자
    participant = [i+1 for i in range(n)]
    
    # 토너먼트 라운드 
    cnt = 1
    while n != 1:
        tournament = []
        
        for i in range(1, n, 2):
            if (participant[i-1] == a or participant[i-1] == b) and (participant[i] == a or participant[i] == b):
                answer = cnt 
                return answer
            else:
                if participant[i-1] == a or participant[i] == a:
                    tournament.append(a)
                elif participant[i-1] == b or participant[i] == b:
                    tournament.append(b)
                else:
                    tournament.append(participant[i])
        cnt += 1
        participant = tournament
        
        n /= 2
        n = int(n)
    return answer