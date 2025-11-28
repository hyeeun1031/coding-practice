def is_prime(x):
    # 1 이하는 소수가 아니다
    if x <= 1:
        return False
    
    # 2부터 √x 까지 나누어보며 약수가 있는지 검사
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False  # 나누어 떨어지면 소수가 아님
    return True


def solution(nums):
    n = len(nums)
    answer = 0
    
    # 서로 다른 3개의 인덱스 i, j, k 를 선택 (i < j < k)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                s = nums[i] + nums[j] + nums[k]  # 세 수의 합
                if is_prime(s):                  # 합이 소수인지 검사
                    answer += 1                  # 소수라면 개수 증가
    
    return answer
