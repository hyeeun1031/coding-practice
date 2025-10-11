def solution(a, b, n):
    answer = 0
    # n: 현재 가진 빈 병 수
    while n >= a:
        exchange = (n // a) * b  # 이번에 교환해서 받는 콜라 병 수
        answer += exchange
        n = (n % a) + exchange   # 남은 빈 병 + 새로 받은 병(마시면 빈 병이 됨)
    return answer
