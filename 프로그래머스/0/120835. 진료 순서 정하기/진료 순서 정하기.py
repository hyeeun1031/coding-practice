def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True) # emergency 내림차순 정렬
    
    rank = {}
    for i in range(len(sorted_emergency)):
        value = sorted_emergency[i]
        rank[value] = i+1 # 각 응급도 순위 매기기
        
    answer = []
    for e in emergency:
        answer.append(rank[e]) 
        
    return answer