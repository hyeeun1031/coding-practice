def solution(arr):
    answer = []          # 결과를 저장할 리스트 초기화
    previous = None      # 이전 원소를 저장할 변수 초기화

    for num in arr:
        if num != previous:
            answer.append(num)  # 현재 원소가 이전 원소와 다르면 추가
            previous = num      # 이전 원소를 현재 원소로 업데이트

    return answer  # 최종 결과 반환
