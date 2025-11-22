def solution(want, number, discount):
    from collections import Counter

    need = dict(zip(want, number))   # 필요한 품목 수량
    answer = 0
    window = Counter(discount[:10])  # 처음 10일 카운트

    # 첫 10일 비교
    if window == need:
        answer += 1

    # 할인 리스트를 슬라이딩 윈도우 방식으로 1칸씩 이동
    for i in range(10, len(discount)):
        # 윈도우에서 이전 항목 제거
        prev = discount[i - 10]
        window[prev] -= 1
        if window[prev] == 0:
            del window[prev]

        # 새로운 항목 추가
        window[discount[i]] += 1

        # 비교
        if window == need:
            answer += 1

    return answer
