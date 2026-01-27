def solution(survey, choices):
    # 각 성격 유형별 점수를 저장할 딕셔너리
    score = {ch: 0 for ch in ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']}

    for s, c in zip(survey, choices):
        disagree, agree = s[0], s[1]  # 비동의 쪽, 동의 쪽
        diff = c - 4  # 4는 0점, 기준점

        if diff < 0:          # 비동의 쪽 점수
            score[disagree] += -diff  # 예: 1 -> -3, 2 -> -2, 3 -> -1 이므로 -diff
        elif diff > 0:        # 동의 쪽 점수
            score[agree] += diff      # 예: 5 -> 1, 6 -> 2, 7 -> 3

    # 지표별로 결과 결정 (동점이면 사전순 빠른 쪽 -> 아래 쌍의 첫 글자가 항상 사전상 앞)
    result = ''
    pairs = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    for a, b in pairs:
        if score[a] >= score[b]:
            result += a
        else:
            result += b

    return result
