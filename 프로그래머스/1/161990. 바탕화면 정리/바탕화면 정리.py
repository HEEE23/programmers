def solution(wallpaper):
    answer = []
    
    wall = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                wall.append([i,j])
    
    x = []
    y = []
    for i in range(len(wall)):
        x.append(wall[i][0])
        y.append(wall[i][1])
        
    answer.extend([min(x), min(y), max(x)+1, max(y)+1])
    return answer