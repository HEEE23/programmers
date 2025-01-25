from collections import defaultdict
def solution(genres, plays):
    answer = []
    
    album = []
    genre = defaultdict(int)
    
    for i in range(len(genres)):
        album.append((i, genres[i], plays[i]))
        genre[genres[i]] += plays[i]
        
    g = []
    for key, value in genre.items():
        g.append((key, value))
    g.sort(key = lambda x : -x[1])
    
    a = []
    for gg in g:
        a.append(gg[0])
    
    album.sort(key = lambda x : (a.index(x[1]),-x[2]))
    
    maxnum = 0
    genrenum = album[0][1]

    while album:
        if album[0][1] == genrenum:
            maxnum += 1
            if maxnum <= 2:
                answer.append(album[0][0])
                album.pop(0)
            else:
                album.pop(0)
        else:
            maxnum = 1
            genrenum = album[0][1]
            answer.append(album[0][0])
            album.pop(0)
                
        
    return answer