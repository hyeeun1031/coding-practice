def solution(s):
    numbers = list(map(int, s.split()))  # 문자열을 공백 기준으로 나누고 정수로 변환
    min_num = min(numbers)
    max_num = max(numbers)
    answer = f"{min_num} {max_num}"
    return answer