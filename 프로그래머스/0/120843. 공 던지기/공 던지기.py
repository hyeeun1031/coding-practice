def solution(numbers, k):
    n = len(numbers)
    move = 2 * (k-1)
    idx = move % n
    return numbers[idx]