from collections import Counter

def solution(a, b, c, d):
    dice = [a, b, c, d]
    counter = Counter(dice)
    values = list(counter.keys())
    counts = list(counter.values())

    if len(counter) == 1:
        # case ①: 네 주사위 모두 같음
        p = values[0]
        return 1111 * p

    elif len(counter) == 2:
        # case ② 또는 ③
        # ex) [4,4,4,1] → counts = [3,1]
        if 3 in counts:
            p = values[counts.index(3)]
            q = values[counts.index(1)]
            return (10 * p + q) ** 2
        else:
            # case ③: 2개+2개
            p, q = values
            return (p + q) * abs(p - q)

    elif len(counter) == 3:
        # case ④: 2개 + 1개 + 1개
        p = values[counts.index(2)]
        q, r = [v for v in values if v != p]
        return q * r

    else:
        # case ⑤: 모두 다름
        return min(dice)
