def solution(score):
    # 평균 점수 계산
    averages = [(s[0] + s[1]) / 2 for s in score]
    
    # 내림차순 정렬된 점수 리스트
    sorted_avg = sorted(averages, reverse=True)
    
    # 각 점수의 순위를 구해 매핑
    rank = {}
    for idx, val in enumerate(sorted_avg):
        if val not in rank:   # 같은 점수는 한 번만 기록
            rank[val] = idx + 1
    
    # 원래 순서대로 순위 매핑
    return [rank[a] for a in averages]
