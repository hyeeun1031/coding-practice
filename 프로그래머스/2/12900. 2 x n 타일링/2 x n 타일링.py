def solution(n):
    # 파이썬에서 큰 수의 자릿수 구분은 언더바(_)를 사용합니다.
    MOD = 1_000_000_007
    
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # 공간 복잡도를 O(1)로 제한하는 변수 스와핑 방식
    prev2 = 1  # f(n-2)
    prev1 = 2  # f(n-1)
    current = 0
    
    for i in range(3, n + 1):
        current = (prev1 + prev2) % MOD
        prev2 = prev1
        prev1 = current
        
    return current