def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        min_val = min(arr)             # 가장 작은 값 찾기
        arr.remove(min_val)            # 해당 값 제거
        return arr