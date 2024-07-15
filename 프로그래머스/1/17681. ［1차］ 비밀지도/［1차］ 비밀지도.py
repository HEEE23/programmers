def solution(n, arr1, arr2):
    answer = []
    
    arr = []
    for i in range(n):
        arr.append(bin(arr1[i] | arr2[i])[2:])
    
    for i in range(n):
        if len(arr[i]) < n:
            arr[i] = arr[i].zfill(n)
            
        arr[i] = arr[i].replace('0', ' ')
        arr[i] = arr[i].replace('1', '#')
    answer = arr
    return answer