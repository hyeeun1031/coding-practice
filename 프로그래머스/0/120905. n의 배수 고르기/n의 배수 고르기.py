def solution(n, numlist):
    result = []  # 결과를 저장할 빈 리스트 생성
    
    for num in numlist:
        if num % n == 0:  # n의 배수인지 확인
            result.append(num)  # n의 배수면 결과 리스트에 추가
    
    return result  # 필터링된 리스트 반환
