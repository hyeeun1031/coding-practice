def solution(brown, yellow):
    total = brown + yellow
    
    # (h - 2) × (w - 2) = yellow
    # yellow = a × b 로 두고 a ≤ b
    for h in range(1, int(yellow**0.5) + 1):
        if yellow % h == 0:
            w = yellow // h  # 내부 가로
            
            # 전체 크기
            H = h + 2  # 세로
            W = w + 2  # 가로

            # brown 조건 검증
            if H * W == total and W >= H:
                return [W, H]
