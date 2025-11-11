def solution(n):
    # n+1 크기의 리스트 생성 (0~n)
    sieve = [True] * (n + 1)
    sieve[0], sieve[1] = False, False  # 0과 1은 소수가 아님

    # 에라토스테네스의 체
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False

    # True 값(소수)의 개수를 반환
    return sum(sieve)
