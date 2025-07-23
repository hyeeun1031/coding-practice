def solution(n):
    i = 1          
    fact = 1        # i! 값을 저장할 변수 (초기값은 1! = 1)

    while True:
        fact *= i   # 현재 i에 대한 팩토리얼 값을 계산 (fact = fact * i)
        if fact > n:
            return i - 1  # n을 넘으면, 이전 i가 조건을 만족하는 가장 큰 수이므로 i-1 반환
        i += 1      # 다음 숫자로 넘어감

