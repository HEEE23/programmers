from collections import Counter
def solution(progresses, speeds):
    answer = []

    work = []
    for i in range(len(progresses)):
        cnt = 0
        # 작업 개발 속도
        for j in range(0,100-progresses[i], speeds[i]):
            if j > 100-progresses[i]:
                break
            cnt += 1
        work.append(cnt)

    for i in range(1,len(work)):
        if work[i-1] > work[i]:
            work[i] = work[i-1]

    cnt = Counter(work) 
    answer = list(cnt.values())
    return answer