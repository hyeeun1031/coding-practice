import math

def solution(arr):
    # 초기값은 첫 번째 원소
    answer = arr[0]
    
    # 배열의 두 번째 원소부터 차례로 최소공배수 계산
    for num in arr[1:]:
        answer = answer * num // math.gcd(answer, num)
    
    return answer
