def solution(chicken):
    service = 0
    coupon = chicken

    while coupon >= 10:
        new_chicken = coupon // 10      # 서비스 치킨 수
        remain_coupon = coupon % 10     # 남은 쿠폰
        service += new_chicken          # 서비스 치킨 누적
        coupon = new_chicken + remain_coupon  # 새로 생긴 쿠폰 + 남은 쿠폰
    
    return service
