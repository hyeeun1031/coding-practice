def solution(strArr):
    count_by_len = {}
    
    for s in strArr:
        L = len(s)
        if L in count_by_len:
            count_by_len[L] += 1
        else:
            count_by_len[L] = 1
        
    return max(count_by_len.values())