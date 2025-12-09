def solution(X, Y):
    countX = [0] * 10
    countY = [0] * 10

    # 각 숫자 빈도수 세기
    for ch in X:
        countX[int(ch)] += 1
    for ch in Y:
        countY[int(ch)] += 1

    result = []

    # 9부터 0까지 공통 등장 최소 개수만큼 포함
    for num in range(9, -1, -1):
        common = min(countX[num], countY[num])
        if common > 0:
            result.append(str(num) * common)

    # 공통이 없으면
    if not result:
        return "-1"

    answer = "".join(result)

    # 0만 여러 개인 경우
    if answer[0] == "0":
        return "0"

    return answer
