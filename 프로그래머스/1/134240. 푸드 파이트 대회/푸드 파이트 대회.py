def solution(food):
    left = ''
    for i in range(1, len(food)):  # 0번(물)은 제외
        left += str(i) * (food[i] // 2)
    return left + '0' + left[::-1]
