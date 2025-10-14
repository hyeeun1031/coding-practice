def solution(k, score):
    hof = []      # 명예의 전당 리스트
    result = []   # 발표 점수 기록 리스트

    for s in score:
        hof.append(s)
        hof.sort(reverse=True)  # 내림차순 정렬 (가장 높은 점수가 앞에)
        
        if len(hof) > k:
            hof.pop()  # k개 초과 시 가장 낮은 점수 제거
        
        result.append(hof[-1])  # 현재 명예의 전당의 최하위 점수 기록

    return result
