def dfs(queen, n, row):
    count = 0
    
    if n == row:
        return 1
    
    # 가로
    for col in range(n):
        queen[row] = col

        for x in range(row):
            # 세로
            if queen[x] == queen[row]: 
                break
                
            # 대각선
            if abs(queen[x]-queen[row]) == (row-x):
                break
        else:
            count += dfs(queen, n, row+1)
            
    return count

def solution(n):
    queen = [0]*n
        
    return dfs(queen, n, 0)