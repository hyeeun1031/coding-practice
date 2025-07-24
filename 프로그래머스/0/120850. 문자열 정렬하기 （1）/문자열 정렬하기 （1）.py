def solution(my_string):
    answer = []
    
    for ch in my_string: 
        if ch.isdigit(): # 문자가 숫자인지 확인
            answer.append(int(ch)) # 숫자라면 정수로 바꿔서 리스트에 추가
    
    answer.sort()
    
    return answer