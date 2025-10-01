def solution(arr):
    n = len(arr)        # 행의 수
    m = len(arr[0])     # 열의 수

    if n > m:  # 행이 더 많으면 → 각 행에 0 추가
        for row in arr:
            row.extend([0] * (n - m))
    elif n < m:  # 열이 더 많으면 → 행 추가
        for _ in range(m - n):
            arr.append([0] * m)
    # 같으면 그대로 반환
    
    return arr
