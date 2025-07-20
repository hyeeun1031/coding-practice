def solution(hp):
    general = hp // 5 # 필요한 장군개미 계산
    remaining_hp = hp % 5 # 남은 체력 계산
    
    solider = remaining_hp // 3 # 남은 체력 중 병정개미 계산
    remaining_hp %= 3 # 남은 체력 계산
    
    worker = remaining_hp # 남은 체력 전부 일개미로 계산
    
    total = general + solider + worker
    return total