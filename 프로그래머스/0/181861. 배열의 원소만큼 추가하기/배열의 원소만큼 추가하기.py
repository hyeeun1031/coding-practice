def solution(arr):
    answer = []
    
    for a in arr:
        answer.extend([a] * a) # [a] * a 는 a를 a번 반복한 리스트
    return answer