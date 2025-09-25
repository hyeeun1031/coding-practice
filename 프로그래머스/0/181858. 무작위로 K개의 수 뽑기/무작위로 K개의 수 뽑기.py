def solution(arr, k):
    seen = set()
    result = []
    
    for num in arr:
        if num not in seen:   # 처음 등장한 값이면
            result.append(num)
            seen.add(num)
            
            if len(result) == k:  # k개 다 채우면 중단
                break
    
    # 모자라면 -1 채우기
    while len(result) < k:
        result.append(-1)
    
    return result