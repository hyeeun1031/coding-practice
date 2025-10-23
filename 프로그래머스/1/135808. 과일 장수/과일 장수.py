def solution(k, m, score):
    score.sort(reverse=True)  # 1️⃣ 내림차순 정렬
    profit = 0

    # 2️⃣ m개씩 묶기
    for i in range(0, len(score), m):
        box = score[i:i+m]
        if len(box) == m:           # 남는 사과는 제외
            profit += min(box) * m  # 3️⃣ 상자 가격 계산

    return profit
