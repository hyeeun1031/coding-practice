def solution(n):
    pizza_count = 1 # 처음에는 피자 한 판으로 시작
    while True:
        total_slices = pizza_count * 6 # 현재 시킨 피자 판 수에 따른 총 조각 수
        if total_slices % n == 0: # 총 조각 수가 n으로 나누어 떨어지면
            return pizza_count # 현재 피자 판 수가 정답
        pizza_count += 1 # 나누어 떨어지지 않으면 피자 한 판 더 추가