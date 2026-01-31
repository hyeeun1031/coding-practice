def solution(dartResult):
    scores = []   # 각 기회별 점수 저장
    num_str = ""  # 숫자를 문자열로 모아두는 용도 (10 처리 포함)

    for ch in dartResult:
        # 1. 숫자인 경우: 이어 붙이기 (10처럼 두 자리 숫자 처리 가능)
        if ch.isdigit():
            num_str += ch

        # 2. 보너스인 경우: 지금까지 모은 숫자를 점수로 만들고 제곱
        elif ch in ['S', 'D', 'T']:
            num = int(num_str)
            num_str = ""  # 숫자 문자열 초기화

            if ch == 'S':
                score = num ** 1
            elif ch == 'D':
                score = num ** 2
            else:  # 'T'
                score = num ** 3

            scores.append(score)

        # 3. 옵션인 경우: *, #
        elif ch == '*':
            # 현재 점수 2배
            scores[-1] *= 2
            # 이전 점수가 있다면 이전 점수도 2배
            if len(scores) > 1:
                scores[-2] *= 2

        elif ch == '#':
            # 현재 점수에 -1 곱하기
            scores[-1] *= -1

    return sum(scores)
