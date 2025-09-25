def solution(arr, queries):
    answer = []
    
    for query in queries:
        s, e, k = query  # 쿼리 해체
        sub_arr = arr[s:e+1]  # 부분 배열
        bigger = []
        
        for num in sub_arr:
            if num > k:
                bigger.append(num)
        
        if bigger:
            answer.append(min(bigger))
        else:
            answer.append(-1)
        
    return answer