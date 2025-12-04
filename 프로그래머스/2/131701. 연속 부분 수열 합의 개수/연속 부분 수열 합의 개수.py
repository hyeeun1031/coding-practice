def solution(elements):
    n = len(elements)
    arr = elements * 2  # 원형 처리를 위해 두 번 이어 붙임
    sums = set()  # 가능한 모든 부분합 저장 (중복 제거)

    # 부분 수열 길이 1부터 n까지
    for length in range(1, n + 1):
        # 시작점 0부터 n-1까지만 보면 됨
        for start in range(n):
            sums.add(sum(arr[start:start + length]))

    return len(sums)
