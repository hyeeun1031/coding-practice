def solution(numbers, n):
    answer = 0  # 합계를 저장할 변수 초기화
    
    for num in numbers:
        answer += num  # 현재 원소를 합계에 더함
        if answer > n:  # 합계가 n보다 큰지 확인
            return answer  # 조건 만족 시 합계를 반환
    
    return answer  # 모든 원소를 더해도 n을 초과하지 않을 경우 최종 합계 반환
