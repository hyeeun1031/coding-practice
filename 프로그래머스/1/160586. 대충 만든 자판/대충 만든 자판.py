def solution(keymap, targets):
    # 1. 각 문자별 최소 누름 횟수 계산
    min_press = {}
    
    for key in keymap:
        for idx, ch in enumerate(key):
            press = idx + 1
            if ch not in min_press:
                min_press[ch] = press
            else:
                min_press[ch] = min(min_press[ch], press)
    
    # 2. target 별 최소 누름 수 계산
    result = []
    for target in targets:
        total = 0
        possible = True
        
        for ch in target:
            if ch not in min_press:
                possible = False
                break
            total += min_press[ch]
        
        result.append(total if possible else -1)
    
    return result
