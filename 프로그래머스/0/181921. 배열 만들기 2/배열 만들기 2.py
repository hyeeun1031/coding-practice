def solution(l, r):
    result = []
    
    for x in range(l, r + 1):
        s = str(x)
        ok = True
        
        for ch in s:
            if ch not in ('0', '5'):
                ok = False
                break
        
        if ok:
            result.append(x)
    
    if not result:
        return [-1]
    return result
