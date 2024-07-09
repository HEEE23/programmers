def solution(sizes):
    answer = 0
    
    x_sizes = []
    y_sizes = []
    for i in range(len(sizes)):
        x, y = sizes[i]
        x_sizes.append(x)
        y_sizes.append(y)
        
    for i in range(len(sizes)):
        tmp = 0
        if (x_sizes[i] < y_sizes[i]):
            tmp = x_sizes[i]
            x_sizes[i] = y_sizes[i]
            y_sizes[i] = tmp
            
    answer = max(x_sizes)*max(y_sizes)
    return answer