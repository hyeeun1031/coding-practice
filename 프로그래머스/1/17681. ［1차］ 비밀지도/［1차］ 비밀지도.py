def solution(n, arr1, arr2):
    result = []
    for i in range(n):
        # 1) OR 연산
        merged = arr1[i] | arr2[i]
        # 2) 이진수로 변환 + 앞자리 0 채우기
        binary = bin(merged)[2:].zfill(n)
        # 3) 1→#, 0→공백으로 변환
        line = binary.replace('1', '#').replace('0', ' ')
        result.append(line)
    return result
