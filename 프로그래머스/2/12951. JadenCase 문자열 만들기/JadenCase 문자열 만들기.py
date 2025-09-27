def solution(s):
    answer = ''
    words = s.split(' ')  # 공백 기준으로 단어 분리 (연속된 공백도 유지)
    
    for word in words:
        if len(word) == 0:  # 공백만 있는 경우
            answer += ' '
        else:
            # 첫 문자가 알파벳이면 대문자 변환, 그 외는 그대로 두고 나머지는 소문자
            answer += word[0].upper() + word[1:].lower() if word[0].isalpha() else word[0] + word[1:].lower()
            answer += ' '
    
    return answer[:-1]  # 마지막에 붙은 불필요한 공백 제거
