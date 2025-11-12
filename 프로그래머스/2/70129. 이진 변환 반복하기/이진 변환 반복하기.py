def solution(s):
    count_transform = 0   # 이진 변환 횟수
    count_zero = 0        # 제거된 0의 총 개수

    while s != "1":
        # 1) 0 제거
        zeros = s.count('0')
        count_zero += zeros

        # 2) 0을 제거한 문자열의 길이 구하기
        s = s.replace('0', '')
        length = len(s)

        # 3) 길이를 2진법 문자열로 변환
        s = bin(length)[2:]

        # 4) 변환 횟수 증가
        count_transform += 1

    return [count_transform, count_zero]
