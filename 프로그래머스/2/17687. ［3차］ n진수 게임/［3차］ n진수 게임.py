def solution(n, t, m, p):
    digits = "0123456789ABCDEF"
    needed = p + (t - 1) * m + 5  # 여유 있게 생성
    s = []
    num = 0
    while len(s) < needed:
        if num == 0:
            s.append('0')
        else:
            x = num
            temp = []
            while x > 0:
                temp.append(digits[x % n])
                x //= n
            s.extend(reversed(temp))
        num += 1

    result = []
    idx = p - 1
    for _ in range(t):
        result.append(s[idx])
        idx += m
    return "".join(result)