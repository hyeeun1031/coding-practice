def solution(n: int) -> int:
    x = 0
    for _ in range(n):
        x += 1
        # 3의 배수이거나 '3'을 포함하면 다음 수로 건너뛰기
        while x % 3 == 0 or '3' in str(x):
            x += 1
    return x
