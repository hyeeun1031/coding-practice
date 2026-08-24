def solution(weights):
    answer = 0
    
    # 몸무게별 등장 횟수
    count = {}
    
    for w in weights:
        count[w] = count.get(w, 0) + 1
    
    # 1. 같은 몸무게
    for w in count:
        if count[w] >= 2:
            answer += count[w] * (count[w] - 1) // 2
    
    # 2. 2 : 3
    # 작은 몸무게 w, 큰 몸무게 3w/2
    for w in count:
        if w * 3 % 2 == 0:
            other = w * 3 // 2
            if other in count:
                answer += count[w] * count[other]
    
    # 3. 1 : 2
    for w in count:
        other = w * 2
        if other in count:
            answer += count[w] * count[other]
    
    # 4. 3 : 4
    for w in count:
        if w * 4 % 3 == 0:
            other = w * 4 // 3
            if other in count:
                answer += count[w] * count[other]
    
    return answer