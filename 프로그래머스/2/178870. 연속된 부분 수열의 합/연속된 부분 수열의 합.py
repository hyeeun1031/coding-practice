def solution(sequence, k):
    n = len(sequence)
    
    start = 0
    current_sum = 0
    
    answer = [0, n - 1]
    min_length = n
    
    for end in range(n):
        current_sum += sequence[end]
        
        # 합이 k 이상이면 왼쪽을 줄인다.
        while current_sum > k:
            current_sum -= sequence[start]
            start += 1
        
        # 합이 k인 경우
        if current_sum == k:
            length = end - start + 1
            
            if length < min_length:
                min_length = length
                answer = [start, end]
    
    return answer