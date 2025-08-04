def solution(num_list, n):
    
    after = num_list[n:]
    before = num_list[:n]
    
    answer = after + before
    
    return answer