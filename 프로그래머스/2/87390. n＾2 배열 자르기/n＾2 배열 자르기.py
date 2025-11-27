def solution(n, left, right):
    result = []
    for k in range(left, right + 1):
        row = k // n
        col = k % n
        result.append(max(row + 1, col + 1))
    return result
