def solution(lines):
    # 각 좌표의 등장 횟수를 저장할 딕셔너리
    counter = {}
    
    # 각 선분의 범위를 순회
    for start, end in lines:
        for x in range(start, end):  # end는 포함하지 않음
            counter[x] = counter.get(x, 0) + 1
    
    # 두 개 이상 겹치는 구간만 카운트
    overlap = sum(1 for v in counter.values() if v >= 2)
    
    return overlap
