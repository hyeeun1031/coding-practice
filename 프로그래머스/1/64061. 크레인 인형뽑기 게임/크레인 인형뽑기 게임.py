def solution(board, moves):
    basket = []
    removed = 0
    n = len(board)

    for move in moves:
        col = move - 1  # 1-indexed → 0-indexed

        for row in range(n):
            if board[row][col] != 0:
                doll = board[row][col]
                board[row][col] = 0  # 인형 제거

                if basket and basket[-1] == doll:
                    basket.pop()
                    removed += 2
                else:
                    basket.append(doll)

                break  # 한 번 집으면 종료

    return removed
