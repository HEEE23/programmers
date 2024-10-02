def solution(prices):
    answer = []
    
    queue = []
    for i in range(len(prices)):
        queue.append(prices[i])
        answer.append(0)
        
        for j in range(i+1, len(prices)):
            answer[i] += 1
            
            if prices[j] < prices[i]:
                break

    return answer