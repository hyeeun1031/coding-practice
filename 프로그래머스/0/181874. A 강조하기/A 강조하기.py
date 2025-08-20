def solution(myString):
    result = ""
    
    for c in myString:
        if c == 'a': # 소문자 a는 대문자 A로 변환
            result += 'A'
        elif c != "A":
            result += c.lower()
        else:
            result += c
    return result