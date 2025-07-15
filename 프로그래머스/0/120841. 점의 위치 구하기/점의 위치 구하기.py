def solution(dot):
    x, y = dot  # 좌표 분리
    if x > 0 and y > 0:
        return 1  # 제1사분면
    elif x < 0 and y > 0:
        return 2  # 제2사분면
    elif x < 0 and y < 0:
        return 3  # 제3사분면
    elif x > 0 and y < 0:
        return 4  # 제4사분면
