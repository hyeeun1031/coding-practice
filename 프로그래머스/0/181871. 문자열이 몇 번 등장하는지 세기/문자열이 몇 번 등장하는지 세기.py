def solution(myString, pat):
    count = 0
    m = len(pat)
    
    for i in range(len(myString)-m+1):
        if myString[i:i+m] == pat:
            count += 1
    return count