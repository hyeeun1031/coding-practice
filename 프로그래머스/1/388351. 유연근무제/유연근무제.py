def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)

    for i in range(n):

        # 인정 시각 계산 (+10분)
        h = schedules[i] // 100
        m = schedules[i] % 100

        total = h * 60 + m + 10
        limit_h = total // 60
        limit_m = total % 60

        limit = limit_h * 100 + limit_m

        ok = True

        for j in range(7):
            day = (startday + j - 1) % 7 + 1

            # 주말 skip
            if day == 6 or day == 7:
                continue

            if timelogs[i][j] > limit:
                ok = False
                break

        if ok:
            answer += 1

    return answer