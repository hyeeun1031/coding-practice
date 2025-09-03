def solution(arr, k):
    # k가 홀수일 경우 각 원소에 k를 곱함, 짝수일 경우 각 원소에 k를 더함
    
    result = []
    for x in arr:
        if k % 2 == 1:      # k가 홀수일 때
            result.append(x * k)
        else:               # k가 짝수일 때
            result.append(x + k)
    return result
