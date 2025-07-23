def solution(strlist):
    result = []  
    for s in strlist:  # strlist 안에 있는 문자열을 하나씩 꺼내서 s에 저장
        length = len(s)  # s의 길이
        result.append(length)  # 구한 길이를 result 리스트에 추가
    return result 
