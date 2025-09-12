def solution(arr):
    n = len(arr)
    power = 1
    
    while power < n:
        power *= 2
        
    need = power - n
    
    return arr + [0] * need