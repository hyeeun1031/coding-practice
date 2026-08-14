def solution(m, n, board):
    board = [list(row) for row in board]
    answer = 0

    while True:
        to_remove = set()
        for i in range(m - 1):
            for j in range(n - 1):
                c = board[i][j]
                if c != ' ' and c == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    to_remove.update([(i, j), (i, j+1), (i+1, j), (i+1, j+1)])

        if not to_remove:
            break

        answer += len(to_remove)
        for i, j in to_remove:
            board[i][j] = ' '

        # 중력 적용: 각 열마다 빈칸이 위로, 블록이 아래로 몰리게 함
        for j in range(n):
            col = [board[i][j] for i in range(m) if board[i][j] != ' ']
            col = [' '] * (m - len(col)) + col
            for i in range(m):
                board[i][j] = col[i]

    return answer