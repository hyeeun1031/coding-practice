def solution(m, n, puddles):
    MOD = 1000000007
    
    # DP 테이블 초기화 (행: n+1, 열: m+1)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 물에 잠긴 지역 표시 (puddles 좌표는 [x, y] 형태이므로 dp[y][x]로 설정)
    puddle_set = {(y, x) for x, y in puddles}
    
    # 집 위치 초기화
    dp[1][1] = 1
    
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            # 집 위치는 건너뜀
            if y == 1 and x == 1:
                continue
            
            # 물에 잠긴 지역이면 경로 수는 0
            if (y, x) in puddle_set:
                dp[y][x] = 0
            else:
                # 위쪽(dp[y-1][x])과 왼쪽(dp[y][x-1])에서 오는 경우의 수의 합
                dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % MOD
                
    return dp[n][m]