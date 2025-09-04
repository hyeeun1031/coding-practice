def solution(a, b):
    minab = min(a,b)
    maxab = max(a,b)
    
    return sum(range(minab, maxab+1))