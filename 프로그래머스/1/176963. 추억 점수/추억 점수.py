def solution(name, yearning, photo):
    # 이름-그리움 점수 매핑
    score_dict = dict(zip(name, yearning))
    
    result = []
    for p in photo:
        total = 0
        for person in p:
            # 해당 인물이 점수 목록에 있다면 더하기
            if person in score_dict:
                total += score_dict[person]
        result.append(total)
    
    return result
