def solution(a, b):
    if a%2 == 1 and b%2 == 1: # 둘 다 홀수
        return a*a + b*b
    elif (a%2 == 1) ^ (b%2 == 1): # 하나만 홀수
        return 2 * (a+b)
    else: # 둘 다 짝수
        return abs(a-b)