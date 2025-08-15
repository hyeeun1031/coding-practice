def solution(my_string, index_list):
    answer = ''
    
    for i in index_list:
        char = my_string[i] # 해당 인덱스에 있는 글자 가져오기
        answer += char # 결과 문자열에 이어붙이기
        
    return answer