def solution(order):
    s = str(order)
    
    count = 0
    for ch in s:
        if ch in ['3','6','9']:
            count += 1
    return count