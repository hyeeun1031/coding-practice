def solution(arr, query):
    for i in range(len(query)):
        if i % 2 == 0:  # 짝수 인덱스 → 뒷부분 자르기
            arr = arr[:query[i] + 1]
        else:           # 홀수 인덱스 → 앞부분 자르기
            arr = arr[query[i]:]
    return arr
