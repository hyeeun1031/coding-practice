def solution(my_string, is_prefix):
    if len(is_prefix) > len(my_string): # 접두사 길이가 원본 문자열보다 길면 바로 0 반환
        return 0
    
    for i in range(len(is_prefix)):
        if my_string[i] != is_prefix[i]: # 한 글자라도 다르면 접두사가 아님
            return 0
    return 1