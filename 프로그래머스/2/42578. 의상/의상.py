def solution(clothes):
    from collections import Counter
    
    # 종류별 의상 개수 세기
    type_count = Counter(kind for _, kind in clothes)
    
    answer = 1
    for count in type_count.values():
        answer *= (count + 1)  # 입지 않는 경우 포함
    
    return answer - 1
