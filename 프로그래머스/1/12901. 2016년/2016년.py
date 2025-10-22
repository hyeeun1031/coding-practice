def solution(a, b):
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    # 1월부터 (a-1)월까지의 일수를 모두 더하고 b-1일을 더함
    total_days = sum(month_days[:a-1]) + (b - 1)
    
    # 요일 인덱스 구하기
    return week[total_days % 7]
