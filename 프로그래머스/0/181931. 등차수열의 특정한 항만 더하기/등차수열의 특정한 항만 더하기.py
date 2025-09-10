def solution(a, d, included):
    total = 0
    for i, inc in enumerate(included):  # i: 0..n-1
        if inc:                         # i+1항을 포함할 때만
            total += a + d * i
    return total
