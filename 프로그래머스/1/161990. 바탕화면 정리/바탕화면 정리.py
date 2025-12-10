def solution(wallpaper):
    # 바탕화면의 크기 (최대 50x50)
    # R: 세로 길이 (행의 개수)
    # C: 가로 길이 (열의 개수)
    R = len(wallpaper)
    C = len(wallpaper[0])
    
    # 드래그 시작점 (lux, luy)와 끝점 (rdx, rdy) 초기화
    # lux: 모든 파일 중 가장 작은 행 인덱스 (min_row)
    # luy: 모든 파일 중 가장 작은 열 인덱스 (min_col)
    # rdx: 모든 파일 중 가장 큰 행 인덱스 + 1 (max_row + 1)
    # rdy: 모든 파일 중 가장 큰 열 인덱스 + 1 (max_col + 1)
    
    # 최소 행/열은 최대 가능한 값으로 초기화
    # 최대 행/열은 최소 가능한 값으로 초기화
    min_r, min_c = R, C
    max_r, max_c = -1, -1
    
    # 바탕화면 순회
    for r in range(R):
        for c in range(C):
            # 파일(#)을 찾으면 경계값 업데이트
            if wallpaper[r][c] == '#':
                # 가장 작은 행 (lux) 업데이트
                min_r = min(min_r, r)
                
                # 가장 작은 열 (luy) 업데이트
                min_c = min(min_c, c)
                
                # 가장 큰 행 (rdx-1) 업데이트
                max_r = max(max_r, r)
                
                # 가장 큰 열 (rdy-1) 업데이트
                max_c = max(max_c, c)
                
    # 결과 배열 구성
    # lux = min_r
    # luy = min_c
    # rdx = max_r + 1 (직사각형이 max_r 행까지 포함해야 하므로, 끝점은 max_r + 1)
    # rdy = max_c + 1 (직사각형이 max_c 열까지 포함해야 하므로, 끝점은 max_c + 1)
    
    return [min_r, min_c, max_r + 1, max_c + 1]