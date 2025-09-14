def solution(s):
    n = len(s)
    if n % 2 == 1:  # 홀수
        return s[n // 2]
    else:           # 짝수
        return s[n//2-1 : n//2+1]