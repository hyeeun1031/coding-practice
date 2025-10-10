import math

def solution(a, b):
    # 1. 기약분수로 만들기
    gcd = math.gcd(a, b)
    b //= gcd  # 분모를 최대공약수로 나눈다.

    # 2. 분모의 소인수 중 2와 5 제거
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5

    # 3. 남은 분모가 1이면 유한소수, 아니면 무한소수
    return 1 if b == 1 else 2
