def solution(order):
    stack = []
    nextBox = 1
    count = 0
    
    for target in order:
        # 벨트에서 자격이 될 때까지 push
        while nextBox <= target:
            stack.append(nextBox)
            nextBox += 1
        
        # 스택 맨 위가 목표 상자인 경우 pop
        if stack and stack[-1] == target:
            stack.pop()
            count += 1
        else:
            break  # 더 이상 실을 수 없음
    
    return count
