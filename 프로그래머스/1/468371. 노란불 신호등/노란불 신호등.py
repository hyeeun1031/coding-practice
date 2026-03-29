from math import gcd
from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(signals):
    # 1. 각 주기 계산
    cycles = [G + Y + R for G, Y, R in signals]
    
    # 2. 전체 LCM 계산
    total_lcm = reduce(lcm, cycles)
    
    # 3. 시간 탐색
    for t in range(1, total_lcm + 1):
        all_yellow = True
        
        for G, Y, R in signals:
            cycle = G + Y + R
            time_in_cycle = (t - 1) % cycle  # 0-based
            
            # 노란불 조건
            if not (G <= time_in_cycle < G + Y):
                all_yellow = False
                break
        
        if all_yellow:
            return t
    
    return -1