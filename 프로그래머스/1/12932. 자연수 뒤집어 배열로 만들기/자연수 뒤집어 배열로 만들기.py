def solution(n):
    answer = list(map(int, str(n)[n::-1]))
    return answer