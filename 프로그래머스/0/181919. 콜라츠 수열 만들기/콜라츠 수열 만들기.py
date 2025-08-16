def solution(n):
    result = [n]  # 시작 값 포함
    
    while n != 1:  # 1이 될 때까지 반복
        if n % 2 == 0:  # 짝수
            n //= 2
        else:           # 홀수
            n = 3 * n + 1
        result.append(n)
    
    return result
