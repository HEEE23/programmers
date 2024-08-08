def solution(id_list, report, k):
    answer = []

    users = []
    complaint = []

    report = list(set(report))
    for r in report:
        u, c = r.split(' ')
        users.append(u)
        complaint.append(c)
    
    dic = {}
    complain_d = {}
    for lst in id_list:
        dic[lst] = []
        for i in range(len(users)):
            if users[i] == lst:
                dic[lst].append(complaint[i])
                if complaint[i] in complain_d:  
                    complain_d[complaint[i]] += 1
                else:
                    complain_d[complaint[i]] = 1

    for lst in id_list:
        count = 0
        for u in dic[lst]:
            if complain_d[u] >= k:
                count += 1
        answer.append(count)

    return answer