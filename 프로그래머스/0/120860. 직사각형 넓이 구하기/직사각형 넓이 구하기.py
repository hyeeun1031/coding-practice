def solution(dots):
    x = [dot[0] for dot in dots]  # x좌표만 추출
    y = [dot[1] for dot in dots]  # y좌표만 추출
    
    width = max(x) - min(x)   # 가로 길이
    height = max(y) - min(y)  # 세로 길이
    
    return width * height     # 넓이 계산
