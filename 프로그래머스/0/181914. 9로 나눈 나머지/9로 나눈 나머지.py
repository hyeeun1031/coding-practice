def solution(number):
    digit_sum = 0
    for ch in number:
        digit_sum += int(ch)
    return digit_sum % 9