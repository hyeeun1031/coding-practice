def solution(arr, n):
    result = []
    
    if len(arr) % 2 == 1: # 배열의 길이가 홀수인 경우
        for i in range(len(arr)): # 길이가 홀수라면 짝수 인덱스에 n을 더함
            if i % 2 == 0: # 짝수 인덱스
                result.append(arr[i]+n)
            else:
                result.append(arr[i])
    else: # 배열의 길이가 짝수인 경우
        for i in range(len(arr)): # 홀수 인덱스
            if i % 2 == 1:
                result.append(arr[i]+n)
            else:
                result.append(arr[i])
    
    return result
                
            