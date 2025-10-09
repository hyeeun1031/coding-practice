def solution(sizes):
    # 각 명함의 가로, 세로를 회전시켜 긴 쪽을 가로로 맞춤
    normalized = [(max(w, h), min(w, h)) for w, h in sizes]
    
    # 가로 중 최대값, 세로 중 최대값 찾기
    max_w = max(w for w, h in normalized)
    max_h = max(h for w, h in normalized)
    
    return max_w * max_h
