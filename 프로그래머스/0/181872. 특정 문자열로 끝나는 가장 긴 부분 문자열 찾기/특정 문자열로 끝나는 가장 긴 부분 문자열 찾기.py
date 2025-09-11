def solution(myString, pat):
    n,m = len(myString), len(pat)
    last = -1
    
    for i in range(n-m+1):
        if myString[i:i+m] == pat:
            last = i
    return myString[:last + m]