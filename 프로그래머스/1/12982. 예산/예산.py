def solution(d, budget):
    d.sort()  # 작은 금액부터 정렬
    total = 0
    count = 0
    
    for money in d:
        if total + money <= budget:
            total += money
            count += 1
        else:
            break  # 예산 초과 시 종료
    
    return count
