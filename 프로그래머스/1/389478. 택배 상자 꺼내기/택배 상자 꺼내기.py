def solution(n, w, num):
    # 현재 층
    row = (num - 1) // w
    pos = (num - 1) % w

    # 현재 열 계산
    if row % 2 == 0:
        col = pos
    else:
        col = w - 1 - pos

    # 전체 층 수
    total_rows = (n - 1) // w + 1

    # 마지막 층에 상자 개수
    last_count = n % w
    if last_count == 0:
        last_count = w

    count = 0

    for r in range(row, total_rows):
        # 마지막 층이 아닌 경우
        if r < total_rows - 1:
            count += 1
        else:
            # 마지막 층
            if r % 2 == 0:
                if col < last_count:
                    count += 1
            else:
                if col >= w - last_count:
                    count += 1

    return count