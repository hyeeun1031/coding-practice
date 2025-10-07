def solution(n):
    count_ones = bin(n).count('1')  # n의 1의 개수
    while True:
        n += 1
        if bin(n).count('1') == count_ones:
            return n
