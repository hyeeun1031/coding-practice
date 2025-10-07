def solution(n):
    base3 = ''
    while n > 0:
        n, r = divmod(n, 3)
        base3 += str(r)
    return int(base3, 3)
