def solution(x, n):
    answer = []
    for i in range(1, n + 1):   # 1부터 n까지 반복
        answer.append(x * i)
    return answer