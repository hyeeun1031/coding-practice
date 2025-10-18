def solution(numbers):
    result = set()  # 중복 제거를 위해 set 사용
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            result.add(numbers[i] + numbers[j])  # 서로 다른 두 수의 합 저장
    
    return sorted(result)  # 오름차순 정렬 후 반환
