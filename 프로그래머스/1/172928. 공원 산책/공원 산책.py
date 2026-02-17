def solution(park, routes):
    h = len(park)
    w = len(park[0])
    
    # 시작 위치 찾기
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                x, y = i, j
    
    # 방향 정의
    direction = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }
    
    # 명령 수행
    for route in routes:
        op, n = route.split()
        n = int(n)
        
        dx, dy = direction[op]
        
        nx, ny = x, y
        valid = True
        
        # 한 칸씩 이동해보며 확인
        for _ in range(n):
            nx += dx
            ny += dy
            
            # 범위 벗어나는지 확인
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                valid = False
                break
            
            # 장애물 확인
            if park[nx][ny] == 'X':
                valid = False
                break
        
        # 문제 없을 때만 위치 갱신
        if valid:
            x, y = nx, ny
    
    return [x, y]
