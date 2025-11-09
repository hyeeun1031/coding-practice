def solution(s: str) -> int:
    answer = 0
    same = diff = 0
    x = None

    for ch in s:
        if x is None:
            x = ch
            same = diff = 0  # 새 구간 시작

        if ch == x:
            same += 1
        else:
            diff += 1

        if same == diff:
            answer += 1
            x = None  # 다음 구간 시작 신호
            same = diff = 0

    # 끝났는데 동일/상이 일치 못했다면 마지막 덩어리 추가
    if x is not None:
        answer += 1

    return answer
