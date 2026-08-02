import math

def solution(fees, records):
    def to_min(t):
        h, m = map(int, t.split(':'))
        return h * 60 + m

    in_time = {}
    total = {}

    for rec in records:
        t, car, action = rec.split()
        t = to_min(t)
        if action == 'IN':
            in_time[car] = t
        else:  # OUT
            total[car] = total.get(car, 0) + (t - in_time.pop(car))

    # 출차 기록 없이 남아있는 차량 -> 23:59 출차로 간주
    for car, t in in_time.items():
        total[car] = total.get(car, 0) + (24 * 60 - 1 - t)

    base_t, base_f, unit_t, unit_f = fees
    result = []
    for car in sorted(total):
        m = total[car]
        fee = base_f
        if m > base_t:
            fee += math.ceil((m - base_t) / unit_t) * unit_f
        result.append(fee)

    return result