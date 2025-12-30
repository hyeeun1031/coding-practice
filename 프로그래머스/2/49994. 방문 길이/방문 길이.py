def solution(dirs):
    x, y = 0, 0
    visited = set()

    # 방향 정의
    move = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }

    for d in dirs:
        dx, dy = move[d]
        nx, ny = x + dx, y + dy

        # 경계 체크
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            # 길은 방향이 없으므로 정렬
            edge = tuple(sorted(((x, y), (nx, ny))))
            visited.add(edge)

            # 좌표 이동
            x, y = nx, ny

    return len(visited)
