def solution(board, k):
    n,m = len(board), len(board[0])
    s = 0
    
    for i in range(n):
        for j in range(m):
            if i + j <= k:
                s += board[i][j]
    return s