def solution(dots):
    def is_parallel(a, b, c, d):
        # (y2 - y1) / (x2 - x1) == (y4 - y3) / (x4 - x3)
        # → 분모 제거를 위해 교차 곱 비교
        return (b[1] - a[1]) * (d[0] - c[0]) == (d[1] - c[1]) * (b[0] - a[0])

    a, b, c, d = dots

    # 세 가지 가능한 조합 검사
    if is_parallel(a, b, c, d): return 1
    if is_parallel(a, c, b, d): return 1
    if is_parallel(a, d, b, c): return 1

    return 0
