def solution(s):
    answer = []
    
    for ch in s:
        if s.count(ch) == 1:
            answer.append(ch)
            
    answer = sorted(answer)
    return "".join(answer)