def solution(routes):
    # 차량의 진출 지점을 기준으로 오름차순 정렬
    routes.sort(key=lambda x: x[1])
    
    camera_count = 0
    camera_position = -30001  # 문제에서 주어진 최소 진입 지점(-30,000)보다 작은 값으로 초기화
    
    for route in routes:
        start, end = route
        
        # 현재 차량의 진입 지점이 마지막 카메라 위치보다 크다면 카메라 추가 설치
        if start > camera_position:
            camera_count += 1
            camera_position = end  # 새로운 카메라를 현재 차량의 진출 지점에 설치
            
    return camera_count