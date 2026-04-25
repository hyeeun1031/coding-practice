from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    
    queue = deque()
    queue.append((0, 0, 1))  # (행, 열, 이동 칸 수)
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        r, c, dist = queue.popleft()
        
        if r == n-1 and c == m-1:
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and maps[nr][nc] == 1:
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))
    
    return -1