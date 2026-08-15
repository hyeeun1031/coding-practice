def solution(numbers):
    answer = []
    for x in numbers:
        y = x + 1
        low = y & -y          # y의 최하위 1비트
        if low == 1:
            answer.append(x + 1)
        else:
            answer.append(x + (low >> 1))
    return answer