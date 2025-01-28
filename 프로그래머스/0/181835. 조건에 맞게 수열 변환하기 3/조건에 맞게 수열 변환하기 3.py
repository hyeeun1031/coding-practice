def solution(arr, k):
    # k가 홀수일 경우 각 원소에 k를 곱함, 짝수일 경우 각 원소에 k를 더함
    return [x * k if k % 2 == 1 else x + k for x in arr]
