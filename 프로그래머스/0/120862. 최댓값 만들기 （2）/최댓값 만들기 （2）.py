def solution(numbers):
    numbers.sort() # 리스트를 오름차순으로 정렬
    
    # 가장 큰 값이 나올 수 있는 경우:
    # 1. 가장 큰 두 수의 곱
    # 2. 가장 작은 두 수의 곱 (음수*음수)
    
    max1 = numbers[-1] * numbers[-2] # 가장 큰 두 수는 리스트 맨 뒤에 존재
    max2 = numbers[0] * numbers[1] # 가장 작은 두 수는 리스트 맨 앞에 존재
    
    return max(max1, max2)