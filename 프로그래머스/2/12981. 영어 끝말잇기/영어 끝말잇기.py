def solution(n, words):
    used = set()
    
    for i in range(len(words)):
        current = words[i]
        
        # 1. 한 글자 단어 검사
        if len(current) <= 1:
            return [(i % n) + 1, (i // n) + 1]
        
        # 2. 이전 단어와 끝말잇기 규칙 검사
        if i > 0:
            prev = words[i - 1]
            if prev[-1] != current[0]:
                return [(i % n) + 1, (i // n) + 1]
        
        # 3. 중복 단어 검사
        if current in used:
            return [(i % n) + 1, (i // n) + 1]
        
        used.add(current)
    
    # 탈락자가 없는 경우
    return [0, 0]
