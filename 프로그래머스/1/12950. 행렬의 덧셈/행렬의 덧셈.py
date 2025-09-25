def solution(arr1, arr2):
    result = []  # 결과를 담을 리스트
    
    # 행 반복
    for i in range(len(arr1)):
        row = []  # 한 행을 담을 리스트
        
        # 열 반복
        for j in range(len(arr1[0])):
            # 같은 위치의 원소끼리 더하기
            row.append(arr1[i][j] + arr2[i][j])
        
        # 완성된 행을 결과에 추가
        result.append(row)
    
    return result
