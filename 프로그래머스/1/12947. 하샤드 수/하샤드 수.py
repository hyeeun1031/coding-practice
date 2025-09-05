def solution(x):
    digit_sum = 0
    
    for d in str(x):
        digit_sum += int(d)
        
    if x % digit_sum == 0:
        return True
    else:
        return False