def count_divisors(n):
    cnt = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            cnt += 1
            if i != n // i:  # 짝이 다르면 하나 더
                cnt += 1
    return cnt

def solution(number, limit, power):
    total = 0
    for i in range(1, number + 1):
        div_cnt = count_divisors(i)
        if div_cnt > limit:
            total += power
        else:
            total += div_cnt
    return total
