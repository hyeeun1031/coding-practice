def solution(n, k):
    # 서비스로 받은 음료수 개수
    service = n // 10
    # 실제 결제할 음료수 수량
    drinks = k - service
    # 총 금액 계산
    return n * 12000 + drinks * 2000
