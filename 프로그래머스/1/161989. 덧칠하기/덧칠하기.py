def solution(n, m, section):
    answer = 0
    painted_end = 0  # 마지막으로 칠한 구역의 끝 번호
    
    for s in section:
        # 아직 칠하지 않은 구간일 경우
        if s > painted_end:
            answer += 1
            painted_end = s + m - 1  # 롤러로 m미터 칠함
    
    return answer
