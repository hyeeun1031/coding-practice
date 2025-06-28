def solution(s):
    count = 0
    for char in s:
        if char == '(':
            count += 1
        else:
            count -= 1
        if count < 0:  # 닫는 괄호가 더 많아지는 순간
            return False
    return count == 0  # 끝났을 때 개수가 정확히 맞아야 함
