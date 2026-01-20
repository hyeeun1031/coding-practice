import math

def to_base_k(n, k):
    res = ''
    while n > 0:
        n, r = divmod(n, k)
        res = str(r) + res
    return res

def is_prime(x):
    if x < 2:      # 0, 1은 소수 아님
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    limit = int(math.isqrt(x))
    for i in range(3, limit + 1, 2):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    # 1) k진수로 변환
    s = to_base_k(n, k)
    
    # 2) 0을 기준으로 자르기
    chunks = s.split('0')
    
    answer = 0
    for ch in chunks:
        if not ch:          # 빈 문자열이면 스킵
            continue
        num = int(ch)       # 10진수로 해석
        if is_prime(num):   # 소수이면 카운트
            answer += 1
    return answer
