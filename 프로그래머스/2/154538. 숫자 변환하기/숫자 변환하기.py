def solution(x, y, n):
    # x와 y가 처음부터 같다면 연산할 필요가 없으므로 0 반환
    if x == y:
        return 0
    
    # dp[i]는 i에서 y를 만들기 위한 최소 연산 횟수
    # 최솟값을 구해야 하므로 무한대(inf)로 초기화
    dp = [float('inf')] * (y + 1)
    dp[y] = 0
    
    # y부터 x까지 거꾸로 내려오며 최적의 횟수를 계산
    for i in range(y, x - 1, -1):
        # 현재 i 위치가 y로부터 도달 불가능한 상태라면 건너뜀
        if dp[i] == float('inf'):
            continue
            
        # 1. n을 더하는 연산의 역연산 (i - n)
        if i - n >= x:
            dp[i - n] = min(dp[i - n], dp[i] + 1)
            
        # 2. 2를 곱하는 연산의 역연산 (i / 2)
        if i % 2 == 0 and i // 2 >= x:
            dp[i // 2] = min(dp[i // 2], dp[i] + 1)
            
        # 3. 3을 곱하는 연산의 역연산 (i / 3)
        if i % 3 == 0 and i // 3 >= x:
            dp[i // 3] = min(dp[i // 3], dp[i] + 1)
            
    # x 위치의 값이 처음 초기화 그대로 무한대라면 x를 y로 만들 수 없는 경우임
    return dp[x] if dp[x] != float('inf') else -1