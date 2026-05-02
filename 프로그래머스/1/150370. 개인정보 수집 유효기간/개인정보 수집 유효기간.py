def solution(today, terms, privacies):
    answer = []
    
    # 날짜를 총 일수로 변환 (모든 달 = 28일)
    def to_days(date):
        y, m, d = map(int, date.split('.'))
        return y * 12 * 28 + m * 28 + d
    
    # 오늘 날짜
    today_days = to_days(today)
    
    # 약관별 유효기간 저장
    term_dict = {}
    for term in terms:
        kind, months = term.split()
        term_dict[kind] = int(months)
    
    # 개인정보별 파기 여부 확인
    for idx, privacy in enumerate(privacies):
        date, kind = privacy.split()
        
        # 수집일 + 유효기간(개월)
        expire_days = to_days(date) + (term_dict[kind] * 28)
        
        # 유효기간 전날까지 보관 가능 → 오늘이 같거나 크면 파기
        if today_days >= expire_days:
            answer.append(idx + 1)
    
    return answer