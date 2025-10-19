def solution(board):
    n = len(board)
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:  # 지뢰가 있으면
                for k in range(8):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                        board[nx][ny] = 2  # 위험지역 표시

    # 안전한 지역 세기 (0인 칸만)
    safe_count = sum(row.count(0) for row in board)
    return safe_count
