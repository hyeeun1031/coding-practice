def solution(price):
    if price >= 500000:
        discount_rate = 0.20
    elif price >= 300000:
        discount_rate = 0.10
    elif price >= 100000:
        discount_rate = 0.05
    else:
        discount_rate = 0.0
    
    discounted_price = price * (1 - discount_rate)
    return int(discounted_price)
