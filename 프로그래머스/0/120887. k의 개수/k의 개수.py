def solution(i, j, k):
    target = str(k)
    total = 0
    
    for num in range(i, j+1):
        s = str(num)
        total += s.count(target)
        
    return total