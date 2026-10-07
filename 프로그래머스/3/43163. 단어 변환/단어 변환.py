from collections import deque

def can_convert(word1, word2):
    # 두 단어가 한 글자만 다른지 확인하는 함수
    diff_count = sum(1 for a, b in zip(word1, word2) if a != b)
    return diff_count == 1

def solution(begin, target, words):
    # target이 words 목록에 없으면 변환할 수 없음
    if target not in words:
        return 0
    
    # BFS를 위한 큐 생성: (현재 단어, 이동 단계 수)
    queue = deque([(begin, 0)])
    visited = set([begin])
    
    while queue:
        current_word, steps = queue.popleft()
        
        # 목표 단어에 도달한 경우 단계 수 반환
        if current_word == target:
            return steps
        
        # words 내 단어 중 한 글자만 다르고 아직 방문하지 않은 단어 탐색
        for word in words:
            if word not in visited and can_convert(current_word, word):
                visited.add(word)
                queue.append((word, steps + 1))
                
    return 0