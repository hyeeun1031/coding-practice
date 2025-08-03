def solution(names):
    answer = []
    
    for i in range(0, len(names), 5):   # 0부터 5씩 증가하며 반복
        answer.append(names[i])     # 각 그룹의 첫번째 사람을 결과에 추가
    
    return answer