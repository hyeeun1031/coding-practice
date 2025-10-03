import math

def solution(n, m):
    gcd = math.gcd(n, m)           # 최대공약수
    lcm = n * m // gcd             # 최소공배수
    return [gcd, lcm]
