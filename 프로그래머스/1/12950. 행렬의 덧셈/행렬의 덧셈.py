def solution(arr1, arr2):
    answer = []
    
    # for i in range(len(arr1)):
    #     result = []
    #     answer.append(result)
    #     for j in range(len(arr1[i])):
    #         result.append(arr1[i][j] + arr2[i][j])
    
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j]+=arr2[i][j]
    
    answer = arr1
    return answer