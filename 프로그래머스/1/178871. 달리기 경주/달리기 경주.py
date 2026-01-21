def solution(players, callings):
    # 선수 이름 -> 현재 위치(인덱스)
    pos = {name: i for i, name in enumerate(players)}
    
    for name in callings:
        idx = pos[name]          # 현재 위치
        front = players[idx-1]   # 바로 앞 선수
        
        # 자리 교체
        players[idx-1], players[idx] = players[idx], players[idx-1]
        
        # 위치 정보 갱신
        pos[name] -= 1
        pos[front] += 1
    
    return players
