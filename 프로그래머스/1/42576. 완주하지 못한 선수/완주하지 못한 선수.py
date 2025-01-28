def solution(participant, completion):
    player_dict = {}
    
    # 참가자 리스트의 이름을 딕셔너리에 추가하고 빈도수 계산
    for player in participant:
        if player in player_dict:
            player_dict[player] += 1
        else:
            player_dict[player] = 1
    
    # 완주자 리스트의 이름을 딕셔너리에서 빼기
    for player in completion:
        player_dict[player] -= 1
    
    # 빈도수가 1인 이름이 완주하지 못한 선수
    for player, count in player_dict.items():
        if count > 0:
            return player
