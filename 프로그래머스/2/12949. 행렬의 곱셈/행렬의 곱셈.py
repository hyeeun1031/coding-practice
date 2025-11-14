def solution(arr1, arr2):
    # 결과 행렬의 크기: arr1의 행 개수 × arr2의 열 개수
    n, m, k = len(arr1), len(arr1[0]), len(arr2[0])
    
    # 결과를 저장할 2차원 리스트 초기화
    result = [[0] * k for _ in range(n)]
    
    # 행렬 곱셈 수행
    for i in range(n):          # arr1의 행
        for j in range(k):      # arr2의 열
            for x in range(m):  # 곱셈·덧셈 반복
                result[i][j] += arr1[i][x] * arr2[x][j]

    return result