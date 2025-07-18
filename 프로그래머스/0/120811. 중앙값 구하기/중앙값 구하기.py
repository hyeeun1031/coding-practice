def solution(array):
    array.sort() # 배열을 오름차순으로 정렬
    
    n = len(array) # 배열의 길이
    
    middle_index = n // 2 # 중앙값의 인덱스 계산
    
    answer = array[middle_index] # 중앙 인덱스 값을 중앙값으로 지정
    
    return answer # 중앙값 반환