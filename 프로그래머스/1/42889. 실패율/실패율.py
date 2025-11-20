def solution(N, stages):
    # 스테이지별 도전(머무르고 있는) 사람 수 계산
    counts = [0] * (N + 2)
    for s in stages:
        counts[s] += 1

    result = []
    total_players = len(stages)  # 도달한 유저 수(스테이지 1부터 시작)

    for stage in range(1, N + 1):
        if total_players == 0:
            fail_rate = 0
        else:
            fail_rate = counts[stage] / total_players
        
        result.append((stage, fail_rate))
        total_players -= counts[stage]   # 다음 스테이지 도달자 수 업데이트

    # 실패율 내림차순, 스테이지 번호 오름차순 정렬
    result.sort(key=lambda x: (-x[1], x[0]))

    # 스테이지 번호만 추출
    return [stage for stage, _ in result]
