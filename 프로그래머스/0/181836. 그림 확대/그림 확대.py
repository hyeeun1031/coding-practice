def solution(picture, k):
    result = []
    for row in picture:
        # 가로 방향 확대: 각 문자를 k번 반복
        expanded_row = ''.join(char * k for char in row)
        # 세로 방향 확대: 같은 행을 k번 추가
        for _ in range(k):
            result.append(expanded_row)
    return result
