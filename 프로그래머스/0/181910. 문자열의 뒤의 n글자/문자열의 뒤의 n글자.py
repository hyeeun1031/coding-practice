def solution(my_string, n):
    answer = ''
    
    start_index = len(my_string) - n # my_string의 길이에서 n만큼 뺀 위치부터 끝까지 반복
    for i in range(start_index, len(my_string)):
        answer += my_string[i] # 하나씩 결과 문자열에 붙이기
    
    return answer