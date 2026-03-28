def solution(friends, gifts):
    n = len(friends)
    
    # 이름 → 인덱스
    name_to_idx = {name: i for i, name in enumerate(friends)}
    
    # 주고받은 횟수
    give = [[0] * n for _ in range(n)]
    
    # 선물 기록 반영
    for g in gifts:
        a, b = g.split()
        i = name_to_idx[a]
        j = name_to_idx[b]
        give[i][j] += 1
    
    # 선물 지수 계산
    score = [0] * n
    for i in range(n):
        for j in range(n):
            score[i] += give[i][j]   # 준 것
            score[i] -= give[j][i]   # 받은 것
    
    # 다음 달 받을 선물 수
    next_gift = [0] * n
    
    # 모든 쌍 비교
    for i in range(n):
        for j in range(i + 1, n):
            
            if give[i][j] > give[j][i]:
                next_gift[i] += 1
            elif give[i][j] < give[j][i]:
                next_gift[j] += 1
            else:
                # 선물 지수 비교
                if score[i] > score[j]:
                    next_gift[i] += 1
                elif score[i] < score[j]:
                    next_gift[j] += 1
                # 같으면 아무 일 없음
    
    return max(next_gift)