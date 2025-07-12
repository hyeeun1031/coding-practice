def solution(s1, s2):
    answer = 0
    
    for item in s1:
        if item in s2:
            answer += 1
            
    return answer