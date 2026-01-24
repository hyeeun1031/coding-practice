def solution(numbers, hand):
    # 키패드를 좌표로 표현 (row, col)
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    
    # 처음 위치
    left_pos = keypad['*']
    right_pos = keypad['#']
    
    result = []
    
    # 편의용 세트
    left_only = {1, 4, 7}
    right_only = {3, 6, 9}
    
    # 주 손 (tie일 때)
    is_right_handed = (hand == "right")
    
    for num in numbers:
        if num in left_only:
            # 왼쪽 열: 왼손 고정
            result.append('L')
            left_pos = keypad[num]
        elif num in right_only:
            # 오른쪽 열: 오른손 고정
            result.append('R')
            right_pos = keypad[num]
        else:
            # 가운데 열: 거리 비교
            target = keypad[num]
            
            # 왼손, 오른손 거리 계산 (맨해튼 거리)
            left_dist = abs(left_pos[0] - target[0]) + abs(left_pos[1] - target[1])
            right_dist = abs(right_pos[0] - target[0]) + abs(right_pos[1] - target[1])
            
            if left_dist < right_dist:
                result.append('L')
                left_pos = target
            elif right_dist < left_dist:
                result.append('R')
                right_pos = target
            else:
                # 거리 같으면 hand 기준
                if is_right_handed:
                    result.append('R')
                    right_pos = target
                else:
                    result.append('L')
                    left_pos = target
    
    return "".join(result)
